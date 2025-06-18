## Setup Instructions

### Clone the Repo

```bash
git clone https://github.com/yourusername/recipe-social-platform.git
cd social_media_platform

### Create Virtual Environment

python -m venv env
env\Scripts\activate  # On Windows
# source env/bin/activate  # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Apply Migrations
python manage.py makemigrations
python manage.py migrate

# Start Redis 
# Windows 
redis-server

# Start Celery worker and beat
celery -A social_media_platform worker --loglevel=info
celery -A social_media_platform beat --loglevel=info

# API Endpoints

POST /user/register – Register as Seller or Customer
POST /user/login – Get JWT tokens
POST /user/customers - Get Customer List
GET /recipe/recipe – List recipes 
POST /recipe/recipe – Add recipe 
POST /recipe/rating – Rate a recipe 


