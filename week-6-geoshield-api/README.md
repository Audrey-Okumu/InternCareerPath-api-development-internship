# 🛡️ GeoShield API - IP Risk Intelligence

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.14+-blue.svg">
  <img src="https://img.shields.io/badge/Django-6.0-green.svg">
  <img src="https://img.shields.io/badge/DRF-3.16-red.svg">
  <img src="https://img.shields.io/badge/Stripe-14.3-purple.svg">
  <img src="https://img.shields.io/badge/Render-Deployed-success.svg">
</div>

<p align="center">
  <strong>A production-ready IP Risk Intelligence API with geolocation, risk scoring, and usage-metered authentication.</strong>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#live-demo">Live Demo</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#api-endpoints">API Endpoints</a> •
  <a href="#pricing">Pricing</a> •
  <a href="#deployment">Deployment</a>
</p>

---

## 📋 **Project Overview**

**GeoShield API** is the capstone project for my 6-week API Development Internship. It's a fully functional, monetized API that provides IP geolocation and risk intelligence with usage-based billing.

This project demonstrates:
- RESTful API design with Django REST Framework
- User authentication with API keys
- Usage tracking and rate limiting
- Stripe integration for subscription billing
- Metered API usage (free tier + paid plans)
- Interactive Swagger documentation
- Production deployment on Render

---

## ✨ **Features**

### **Core API Features**
- **IP Geolocation** - Country, city, coordinates, and ISP information
- **Risk Scoring** - Identify VPNs, proxies, and malicious IPs
- **API Key Authentication** - Secure bearer token authentication
- **Usage Tracking** - Monthly request counting with auto-reset

### **Developer Portal**
- **User Authentication** - Signup, login, logout
- **Developer Dashboard** - View API key and usage statistics
- **API Key Management** - Copy and regenerate API keys
- **Subscription Plans** - Free tier with upgrade options
- **API Documentation** - Interactive Swagger/ReDoc

### **Billing Integration**
- **Free Tier** - 1,000 requests/month (no credit card)
- **Pro Plan** - 50,000 requests/month ($29/month)
- **Business Plan** - 250,000 requests/month ($99/month)
- **Stripe Integration** - Secure payment processing
- **Usage Metering** - Automatic billing for paid tiers

---

## 🌐 **Live Demo**

The API is live and accessible at:
[Geoshield API](https://geofield-api.onrender.com)


| Resource | URL |
|----------|-----|
| **Landing Page** | [https://geofield-api.onrender.com/](https://geofield-api.onrender.com/) |
| **Pricing** | [https://geofield-api.onrender.com/billing/pricing/](https://geofield-api.onrender.com/billing/pricing/) |
| **Sign Up** | [https://geofield-api.onrender.com/developers/signup/](https://geofield-api.onrender.com/developers/signup/) |
| **API Docs** | [https://geofield-api.onrender.com/swagger/](https://geofield-api.onrender.com/swagger/) |

---

## 🛠️ **Tech Stack**

| Category | Technology |
|----------|------------|
| **Backend Framework** | Django 6.0 + Django REST Framework 3.16 |
| **Database** | PostgreSQL (via Render) |
| **Geolocation** | MaxMind GeoLite2 |
| **Payments** | Stripe API |
| **Authentication** | Custom API Key Authentication |
| **Documentation** | drf-yasg (Swagger/ReDoc) |
| **Hosting** | Render (Web Service + PostgreSQL) |
| **Static Files** | WhiteNoise |
| **Version Control** | Git + GitHub |

---

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.14+
- PostgreSQL (or SQLite for local development)
- Stripe account (for payment processing)
- MaxMind license key (for geolocation)

### **Local Installation**

1. **Clone the repository**
   ```bash
   git clone https://github.com/Audrey-Okumu/InternCareerPath-api-development-internship.git
   cd InternCareerPath-api-development-internship/week-6-geoshield-api
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4  **Create .env file**
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   DATABASE_URL=sqlite:///db.sqlite3  # or postgresql://...
   STRIPE_SECRET_KEY=sk_test_your_stripe_key
   STRIPE_PRICE_ID=price_your_price_id
   MAXMIND_LICENSE_KEY=your_maxmind_key
   ```
5 **Run migrations**
   ```bash
   python manage.py migrate
   ```
6 **Download GeoLite2 database**
   ```bash
   mkdir -p geo_db
   curl -L -o geo_db/GeoLite2.tar.gz "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=$MAXMIND_LICENSE_KEY&suffix=tar.gz"
   tar -xzf geo_db/GeoLite2.tar.gz --strip-components=1 -C geo_db
```
7 **Start the development server**
   ```bash
   python manage.py runserver
   ```


