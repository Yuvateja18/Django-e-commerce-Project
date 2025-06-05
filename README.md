# 🛒 Django E-commerce Project

A basic Django-based e-commerce project with user authentication and admin-powered product management.
This project allows registered users to view products while the admin can manage product listings and categories.

---

## ✅ Features

- 🔐 User registration, login, and logout
- 🧑‍💼 Admin panel to:
  - Add/edit/delete product categories
  - Add/edit/delete products
- 🛍️ Users can browse all available products
- 🖥️ Clean and responsive frontend design

---

## 🛠️ Technologies Used

- **Framework**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap (for UI styling)
- **Database**: SQLite (default with Django)
- **Authentication**: Django's built-in auth system

---

## 📁 Project Structure
Django-e-commerce-Project/
├── firstProject/                  # Main project configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py               # Project settings
│   ├── urls.py                   # URL routing
│   └── wsgi.py
│
├── firstApp/                     # Main application
│   ├── __init__.py
│   ├── admin.py                  # Register models for Django admin
│   ├── apps.py
│   ├── models.py                 # Models for Product & Category
│   └── views.py                  # View functions
|
|
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── signup.html
│   ├── store.html
│   └── Welcome.html
│
├── media/                        # Uploaded media files (e.g., product images)
│
├── db.sqlite3                    # SQLite database file
├── manage.py                     # Django's CLI utility
└── README.md                     # Project documentation (you’re editing this!)

