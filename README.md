# Pyshop

Django e-commerce shop with product catalog, cart, checkout, and order management.

## Features

- Product listing with category filtering and search
- Product detail pages
- Shopping cart (session-based for guests, user-based for logged-in users)
- Checkout and order history
- Admin panel for managing products, categories, offers, and orders
- Image upload support for products

## Requirements

- Python 3.10+
- Django 5.2
- Pillow

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://127.0.0.1:8000/products/` to browse the shop and `/admin/` for the admin panel.
