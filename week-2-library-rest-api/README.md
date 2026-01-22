# 📚 Library REST API (Week 2)

## Overview

This project is a simple **RESTful API** built using **Django** and **Django REST Framework** for managing books in a library system.
It supports full **CRUD operations** (Create, Read, Update, Delete) and follows REST principles.

---

## Features

* Retrieve all books
* Retrieve a single book by ID
* Add a new book
* Update an existing book
* Delete a book
* JSON-based API responses
* SQLite database
* Django Admin support

---

## Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework**
* **SQLite (default Django database)**
---

## 🔗 API Endpoints

### 1️⃣ Get All Books

**GET**

```
/api/books/
```

### 2️⃣ Create a New Book

**POST**

```
/api/books/
```

### 3️⃣ Get a Book by ID

**GET**

```
/api/books/{id}/
```
---

### 4️⃣ Update a Book

**PUT**

```
/api/books/{id}/
```
### 5️⃣ Delete a Book

DELETE

/api/books/{id}/

 ---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
git clone <https://github.com/Audrey-Okumu/InternCareerPath-api-development-internship.git>
cd week-2-library-rest-api

### 2️⃣ Create and activate virtual environment
python -m venv env
env\Scripts\activate   # Windows

### 3️⃣ Install dependencies
pip install django djangorestframework

### 4️⃣ Run migrations
python manage.py migrate

### 5️⃣ Start the development server
python manage.py runserver

## 🔐 Django Admin

### Create an admin user:

python manage.py createsuperuser

### Access admin panel:

http://127.0.0.1:8000/admin/

 ---

## 📌 Learning Outcomes

- Built REST APIs using Django REST Framework
- Implemented function-based views with multiple HTTP methods
- Used serializers for JSON ↔ Python conversion
- Handled HTTP status codes properly
- Structured a real-world backend project