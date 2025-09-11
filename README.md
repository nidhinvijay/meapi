
🛠 Tech Stack

Backend: Python 3.11, Django, Django REST Framework

Database: SQLite (dev) | PostgreSQL (prod on Render)

Server: Gunicorn (via Procfile)

Deployment: Render (Free Tier)

📂 Project Structure
.
├── api/                   # Django app (models, views, serializers, fixtures)
│   └── fixtures/
│       └── initial_data.json
├── server/                # Project configuration (settings, wsgi, asgi)
├── static/                # Project static assets (CSS, JS, images)
├── templates/             # HTML templates
├── manage.py              # Django management CLI
├── requirements.txt       # Python dependencies
├── render.yaml            # Render deployment configuration
├── Procfile               # Gunicorn start command
├── .gitignore             # Ignored files
└── README.md

🚀 Getting Started
1️⃣ Local Setup
# Clone the repository
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

2️⃣ Database Setup
python manage.py migrate
python manage.py loaddata api/fixtures/initial_data.json

3️⃣ Running Locally
python manage.py runserver


API Base URL → http://127.0.0.1:8000/

Admin Panel → http://127.0.0.1:8000/admin/

🔑 Environment Variables

The app requires the following environment variables:

Key	Example Value	Description
DJANGO_SETTINGS_MODULE	server.settings	Django settings module
PYTHON_VERSION	3.11	Python runtime version
DJANGO_SECRET_KEY	b^m4@z!r9f....	Secret key for Django security
DEBUG	False	Set True in local dev, False in production

👉 Generate a new secret key:

python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

🖼 Static Files

Before deployment, collect static files:

python manage.py collectstatic --noinput


Local → served from /static/

Render → stored in /staticfiles/

☁️ Deployment Guide (Render)
Render Config (render.yaml)
services:
  - type: web
    name: me-api
    env: python
    region: singapore
    plan: free
    buildCommand: |
      pip install -r requirements.txt
      python manage.py migrate
      python manage.py collectstatic --noinput
      python manage.py loaddata api/fixtures/initial_data.json || true
    startCommand: gunicorn server.wsgi --preload --bind 0.0.0.0:$PORT
    envVars:
      - key: DJANGO_SETTINGS_MODULE
        value: server.settings
      - key: PYTHON_VERSION
        value: 3.11
      - key: DJANGO_SECRET_KEY
        sync: false

Steps

Push repo to GitHub/GitLab.

Connect repo on Render Dashboard
.

Render auto-detects render.yaml.

Deploy → API will be available at https://me-api.onrender.com/.

✨ Features

Django REST API with DRF

Token-based authentication

Fixtures for quick database setup

Static & media file handling

Production-ready via Gunicorn + Render

Modular, extensible codebase

📌 API Endpoints (Sample)
Endpoint	Method	Description
/api/	GET	API root
/api/items/	GET	List all items
/api/items/	POST	Create new item
/api/items/<id>/	GET	Retrieve item
/api/items/<id>/	PUT/PATCH	Update item
/api/items/<id>/	DELETE	Delete item
