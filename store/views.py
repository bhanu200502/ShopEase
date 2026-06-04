from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Category, Product, Cart, CartItem, Order, OrderItem

# ==================== HOME ====================
def home(request):
    products = Product.objects.filter(stock__gt=0)[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'products': products,
        'categories': categories
    })

# ==================== PRODUCT LIST ====================
def product_list(request):
    products = Product.objects.filter(stock__gt=0)
    categories = Category.objects.all()

    # Search
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)

    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category__id=category_id)

    # Sort by price
    sort = request.GET.get('sort')
    if sort == 'low':
        products = products.order_by('price')
    elif sort == 'high':
        products = products.order_by('-price')

    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
        'sort': sort
    })

# ==================== PRODUCT DETAIL ====================
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'store/product_detail.html', {
        'product': product
    })

# ==================== REGISTER ====================
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')

    return render(request, 'store/register.html')

# ==================== LOGIN ====================
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {username}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('login')

    return render(request, 'store/login.html')

# ==================== LOGOUT ====================
def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

# ==================== CART ====================
@login_required
def cart(request):
    cart_obj, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart_obj)
    total = cart_obj.get_total()
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'total': total
    })

@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart_obj, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart_obj,
        product=product
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, f'{product.name} added to cart!')
    return redirect('cart')

@login_required
def remove_from_cart(request, pk):
    cart_obj = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, pk=pk, cart=cart_obj)
    cart_item.delete()
    messages.success(request, 'Item removed from cart!')
    return redirect('cart')

@login_required
def update_cart(request, pk):
    cart_obj = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, pk=pk, cart=cart_obj)
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

# ==================== CHECKOUT ====================
@login_required
def checkout(request):
    cart_obj = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart_obj)
    total = cart_obj.get_total()

    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']

        # Create Order
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            full_name=full_name,
            phone=phone,
            address=address,
            city=city,
            state=state,
            pincode=pincode
        )

        # Create Order Items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )
            # Reduce stock
            item.product.stock -= item.quantity
            item.product.save()

        # Clear Cart
        cart_items.delete()

        messages.success(request, 'Order placed successfully!')
        return redirect('order_success', pk=order.pk)

    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'total': total
    })

# ==================== ORDER SUCCESS ====================
@login_required
def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'store/order_success.html', {
        'order': order
    })

# ==================== ORDER LIST ====================
@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'store/order_list.html', {
        'orders': orders
    })

# ==================== ORDER DETAIL ====================
@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    order_items = OrderItem.objects.filter(order=order)
    return render(request, 'store/order_detail.html', {
        'order': order,
        'order_items': order_items
    })

# ==================== DASHBOARD ====================
@login_required
def dashboard(request):
    orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, 'store/dashboard.html', {
        'orders': orders
    })