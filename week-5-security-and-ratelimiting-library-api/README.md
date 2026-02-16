# 📚 Security and Rate Limiting (Week 5)

## Overview

This project is an evolution of the Week 2 project with additional features and improvements.It implements a Secure API Gateway designed to protect backend services from unauthorized access, abuse, and distributed attacks.

The gateway integrates:

- API Key Authentication
- JWT-based Authentication
- Rate Limiting using Redis
- Reverse Proxy & Security Hardening via Nginx

The goal is to simulate a production-grade security layer that sits between clients and backend services.

---
## 🚀 Installation & Setup
### Clone Repository
```bash
git clone <repo-url>
cd week5-secure-api-gateway
```
###  Install Dependencies
```bash
pip install -r requirements.txt
```
###  Start Redis

---
## Tech Stack

* **Python 3**
* **Django**
* **Django REST Framework**
* **SQLite (default Django database)**
* **Redis**
* **Nginx**
---

## 🛡️ DDoS Mitigation Strategy

This project defends against:

- Brute-force login attempts
- Token abuse
- API scraping
- Flood attacks
- Excessive connection attempts

Defense layers:

- Nginx request throttling
- Redis rate limiting
- JWT verification
- API key validation
