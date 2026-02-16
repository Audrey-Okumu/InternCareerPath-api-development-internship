# 🚀 Week 4 – Advanced Backend Features

Project: Pagination, Sorting & Filtering (Cursor-Based)

## 📌 Overview

This project enhances a Django REST Library API by implementing efficient data retrieval mechanisms suitable for production-scale systems.

This project implements:

- Cursor-Based Pagination
- Flexible Sorting
- Dynamic Filtering
- Optimized SQL queries

The goal is to simulate how large platforms handle millions of records efficiently.

---

## 🏗️ Architecture

Client → Django REST API → SQL Database

### Large dataset handling flow:

Request → Query Optimization → Indexed Lookup → Cursor Response

---

## 🛠 Tech Stack

Python 3.x
Django
Django REST Framework
PostgreSQL 

---

## 🚀 Installation & Setup

### Clone Repository
```bash
git clone <repo-url>
cd week-4-advanced-library-api
```

### Setup Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

###  Install Dependencies
```bash
pip install django djangorestframework django-filter psycopg2
```

###  Run Migrations
```bash
python manage.py migrate
```
### Start Server
```bash
python manage.py runserver
```
