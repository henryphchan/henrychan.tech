### Django CRUD Project in Retail Environment ###

# Overview
This project is a Django-based CRUD (Create, Read, Update, Delete) application for managing information in a retail environment. The project allows users to create, edit, view, and delete suppliers, including relevant details like contact information, contract dates, and status.

# Project Setup

## Prerequisites
Make sure you have the following installed on your machine:
- Python 3.8+
- Django 3.0+
- Virtualenv (optional, but recommended)

## Tested Environment
This project has been tested in Python 3.10.11 and Django 5.1.3

## Installation

### 1. Clone the Repository
Clone the project from the GitHub repository:
```sh
$ git clone <repository-url>
$ cd retail_project
```

### 2. Create a Virtual Environment
It is recommended to create a virtual environment to manage dependencies:
```sh
$ python -m venv venv
```
Activate the virtual environment:
- On Windows:
  ```sh
  $ venv\Scripts\activate
  ```
- On Linux or macOS:
  ```sh
  $ source venv/bin/activate
  ```

### 3. Install Requirements
Install the required libraries using `pip`:
```sh
$ pip install -r requirements.txt
```

### 4. Migrate the Database
Apply the migrations to set up your database:
```sh
$ python manage.py makemigrations supplier_app
$ python manage.py migrate
```

### 5. Create a Superuser (Optional)
Create an admin user to manage the project through the Django admin site:
```sh
$ python manage.py createsuperuser
```
Follow the prompts to create a new superuser.

### 6. Run the Server
Run the development server to test the application:
```sh
$ python manage.py runserver
```

# Running the Project

1. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to access the main page.

# Flowbite Integration
This project uses Flowbite as a CSS framework via CDN. Flowbite is used for the overall styling of components like forms, buttons, and toast messages to ensure a modern and consistent look.

# License
This project is licensed under the MIT License.

# Contributing
Contributions are welcome! Please open a pull request or issue if you have suggestions or find any bugs.
