# 🍽️ Recipe Management API - Django Ninja 🛠️

A simple **Recipe Management API** built with **Django** and **Django Ninja** that supports **CRUD operations** for managing recipes.

## 🚀 Features
- 📌 Add new recipes with ingredients and cooking steps
- 📌 Retrieve all or specific recipes
- 📌 Update existing recipes
- 📌 Delete recipes
- 📌 API documentation available at `/api/docs`

## ⚡ Tech Stack
- **Django** (Backend Framework)
- **Django Ninja** (Fast API handling)
- **SQLite** (Default Database)
- **Pydantic** (Data Validation)
- **GitHub** (Version Control)

## 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/RecipePro.git
cd RecipePro

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Create a superuser (optional)
python manage.py createsuperuser

# Run the server
python manage.py runserver
