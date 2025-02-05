# Django Authentication App

This project is a Django-based authentication application that includes features such as user registration, login, logout, password reset, and password change functionalities. 

## **Features**
- User Registration with form validation.
- User Login and Logout.
- Password Change functionality.
- Forgot Password and Password Reset via email.
- Profile Management.
- Dashboard for authenticated users.

## **Setup Instructions**

### **Prerequisites**
- Python 3.10 or later
- Django 5.1.3
- Virtual Environment (recommended)

### **Installation Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/Deep3123/Authentication-App
   cd Authentication-App

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate    # On Linux/Mac
   venv\Scripts\activate       # On Windows

3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Configure your database settings in settings.py: By default, the project uses SQLite.   You can update to use a different database backend if needed.

5. Apply migrations:
   ```bash
   python manage.py migrate

6. Create a superuser (admin account):
   ```bash
   python manage.py createsuperuser

7. Start the development server:
   ```bash
   python manage.py runserver

8. Access the application:
 - Admin Panel: http://127.0.0.1:8000/admin/
 - Login Page: http://127.0.0.1:8000/accounts/login/

## Folder Structure
    auth_app/
    ├── accounts/
    │   ├── templates/accounts/
    │   │   ├── base.html
    │   │   ├── login.html
    │   │   ├── signup.html
    │   │   ├── forgot_password.html
    │   │   ├── password_reset_done.html
    │   │   ├── password_reset_email.html
    │   │   ├── password_reset_confirm.html
    │   │   ├── password_reset_complete.html
    │   │   ├── dashboard.html
    │   │   ├── profile.html
    │   │   └── change_password.html
    │   ├── views.py
    │   ├── forms.py
    │   ├── urls.py
    │   ├── models.py
    │   └── admin.py
    ├── auth_app/
    │   ├── settings.py
    │   ├── urls.py
    │   ├── wsgi.py
    │   └── asgi.py
    └── manage.py

## Additional Notes
 - Email functionality for password reset is set to use the Django console email backend for local development. Update the EMAIL_BACKEND settings in settings.py for production use.
 - Default success URLs for password reset and password change can be modified as needed.