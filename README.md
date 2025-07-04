# My Expense Tracker API Project

This is my another big project building a REST API. The goal was to make a system for people to track their money, somethings expenses and income. It's got user logins and stuff so everyone can only see their own money, unless you're, an admin.

### What it Does

* **Users!** You can sign up and log in. Every API needs you to be logged in with a special token.
* **Your Money:** You can add new expenses or income, see all your past ones, change them, or delete them. 
* **Admins Rule:** If you're a superuser (like me, the developer!), you can see EVERYONE'S money records. 
* **Automatic Tax!** it calculates tax for you. Can be a flat amount or a percentage. It adds it to the total.
* **Lots of Records? No Problem!** The API shows records in pages, so it doesn't send everything at once.

## What I Used to Build This (Technologies)

* Backend: Django (the web framework)
* API Part: Django REST Framework (DRF)
* Logins: djangorestframework-simplejwt (for those JWT tokens)
* Database: MySql 
* Python: Version 3.8 or newer needed

## How to Get This Running (Setup)

Okay, so if you wanna try this out, here's how:

1.  **Get the Code:**
    ```bash
    git clone <your-repo-url>
    cd <your-project-directory-name> 
    ```

2.  **Make a Virtual Environment:**
    You should really use a virtual environment for Python projects. It keeps things tidy.
    ```bash
    python3 -m venv venv
    ```
    * **If you're on Mac/Linux:**
        ```bash
        source venv/bin/activate
        ```
    * **If you're on Windows:**
        ```bash
        .\venv\Scripts\activate
        ```

3.  **Install All the things:**
    This command installs all the Python libraries the project needs.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Database Stuff:**
    You gotta apply the database changes.
    ```bash
    python manage.py migrate
    ```

5.  **Make an Admin (Superuser):**
    If you want to be able to see all data, make a superuser. 
    ```bash
    python manage.py createsuperuser
    ```
    (Remember the username and password you type!)

6.  **Start the Server!**
    ```bash
    python manage.py runserver
    ```
    Now the API should be live at `http://127.0.0.1:8000/`.

## API Endpoints (How to Use It)

All the API calls, except for signing up and logging in, need an `access` token. You put it in the `Authorization` header like this: `Authorization: Bearer <your-token-here>`.

### Authentication Stuff

* `POST /api/auth/register/` - To sign up.
* `POST /api/auth/login/` - To log in and get your tokens.
* `POST /api/auth/refresh/` - If your access token runs out, use this with your refresh token to get a new one.

**Example for Register (POST):**
URL: `http://127.0.0.1:8000/api/auth/register/`
Body (JSON):
```json
{
    "username": "myfirstuser",
    "email": "myfirst@example.com",
    "password": "supersecurepassword"
}