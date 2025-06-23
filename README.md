Recipe Management API – Django Ninja
This is a simple Recipe Management API developed using Django and Django Ninja. It provides a basic backend for managing recipes, including operations to create, read, update, and delete recipe entries.

Features
Add new recipes with ingredients and cooking steps

Retrieve all recipes or a specific recipe by ID

Update existing recipe information

Delete recipes

Automatically generated API documentation is available at /api/docs

Tech Stack
Django (Web Framework)

Django Ninja (Fast and modern API handling)

SQLite (Database used for development)

Pydantic (For request and response validation)

Git and GitHub (Version control)

Installation
To run this project locally, follow the steps below:

Clone the repository
git clone https://github.com/YOUR_USERNAME/RecipePro.git
cd RecipePro

Create a virtual environment
For Mac/Linux: source venv/bin/activate
For Windows: venv\Scripts\activate

Install the required dependencies
pip install -r requirements.txt

Apply migrations to set up the database
python manage.py migrate

Start the development server
python manage.py runserver

You can access the API at: http://127.0.0.1:8000/api/
API documentation is available at: http://127.0.0.1:8000/api/docs
