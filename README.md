Me-API Playground

A simple Django REST API project using Django + DRF + SQLite with deployment setup for Render.

🚀 Setup Instructions

Clone the repository

git clone https://github.com/nidhinvijay/meapi.git
cd meapi


Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Run migrations

python manage.py migrate


Load sample data

python manage.py loaddata api/fixtures/initial_data.json


Start development server

python manage.py runserver


Visit: http://127.0.0.1:8000/

📦 Deployment (Render)

https://me-api-ym5n.onrender.com/