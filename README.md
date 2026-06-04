# ShopEase - E-Commerce Web Application

## Project Overview
ShopEase is a fully functional e-commerce web application
built using Django (Python) and SQLite database.
This project was developed as an internship project.

## Technologies Used
- **Backend:** Python, Django 5.2
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite
- **Authentication:** Django Built-in Auth

## Features
- User Registration & Login
- Product Listing & Search
- Filter by Category
- Sort by Price
- Shopping Cart
- Checkout System
- Order Management
- Order Tracking
- User Dashboard
- Admin Panel

## Project Structure
ShopEase/
├── shopease/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── store/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/
│   └── store/
│       ├── base.html
│       ├── home.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── register.html
│       ├── login.html
│       ├── cart.html
│       ├── checkout.html
│       ├── order_success.html
│       ├── order_list.html
│       ├── order_detail.html
│       └── dashboard.html
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── media/
├── manage.py
└── README.md

## Installation Steps

### 1. Clone or Download the project
cd D:
mkdir ShopEase
cd ShopEase

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### 3. Install Requirements
pip install django pillow

### 4. Run Migrations
python manage.py makemigrations
python manage.py migrate

### 5. Create Superuser
python manage.py createsuperuser

### 6. Run Server
python manage.py runserver

### 7. Open Browser
http://127.0.0.1:8000/

## Admin Panel
http://127.0.0.1:8000/admin/

## Pages
| Page | URL |
|------|-----|
| Home | / |
| Products | /products/ |
| Register | /register/ |
| Login | /login/ |
| Cart | /cart/ |
| Checkout | /checkout/ |
| Orders | /orders/ |
| Dashboard | /dashboard/ |

## Database Models
- Category
- Product
- Cart
- CartItem
- Order
- OrderItem

## Developer
- Name: Your Name
- Course: Your Course
- College: Your College
- Year: 2024