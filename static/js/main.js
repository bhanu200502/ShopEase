// ==================== AUTO HIDE MESSAGES ====================
document.addEventListener('DOMContentLoaded', function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(function(message) {
        setTimeout(function() {
            message.style.transition = 'opacity 0.5s';
            message.style.opacity = '0';
            setTimeout(function() {
                message.remove();
            }, 500);
        }, 3000);
    });
});

// ==================== SEARCH VALIDATION ====================
const searchForm = document.querySelector('.search-form');
if (searchForm) {
    searchForm.addEventListener('submit', function(e) {
        const searchInput = searchForm.querySelector('.search-input');
        if (searchInput.value.trim() === '') {
            e.preventDefault();
            searchInput.focus();
        }
    });
}

// ==================== QUANTITY VALIDATION ====================
const qtyBtns = document.querySelectorAll('.qty-btn');
qtyBtns.forEach(function(btn) {
    btn.addEventListener('click', function(e) {
        const value = parseInt(btn.value);
        if (value < 1) {
            if (!confirm('Remove this item from cart?')) {
                e.preventDefault();
            }
        }
    });
});

// ==================== FORM VALIDATION ====================
const checkoutForm = document.querySelector('.checkout-form form');
if (checkoutForm) {
    checkoutForm.addEventListener('submit', function(e) {
        const phone = checkoutForm.querySelector('[name="phone"]');
        const pincode = checkoutForm.querySelector('[name="pincode"]');

        // Phone validation
        if (phone.value.trim().length < 10) {
            e.preventDefault();
            alert('Please enter a valid 10-digit phone number!');
            phone.focus();
            return;
        }

        // Pincode validation
        if (pincode.value.trim().length < 6) {
            e.preventDefault();
            alert('Please enter a valid 6-digit pincode!');
            pincode.focus();
            return;
        }
    });
}

// ==================== REGISTER FORM VALIDATION ====================
const registerForm = document.querySelector('.auth-form');
if (registerForm) {
    registerForm.addEventListener('submit', function(e) {
        const password = registerForm.querySelector('[name="password"]');
        const confirmPassword = registerForm.querySelector('[name="confirm_password"]');

        if (password && confirmPassword) {
            if (password.value !== confirmPassword.value) {
                e.preventDefault();
                alert('Passwords do not match!');
                confirmPassword.focus();
                return;
            }

            if (password.value.length < 6) {
                e.preventDefault();
                alert('Password must be at least 6 characters!');
                password.focus();
                return;
            }
        }
    });
}

// ==================== NAVBAR ACTIVE LINK ====================
const currentPath = window.location.pathname;
const navLinks = document.querySelectorAll('.nav-links a');
navLinks.forEach(function(link) {
    if (link.getAttribute('href') === currentPath) {
        link.style.borderBottom = '2px solid white';
        link.style.paddingBottom = '3px';
    }
});