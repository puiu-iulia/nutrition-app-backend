# nutrition-app-backend

# My Nutrition App API

# Build & run commands

docker-compose build
docker-compose up

# Migrate the db

docker-compose run app sh -c "python manage.py migrate"

# Create superuser

docker-compose run app sh -c "python manage.py createsuperuser"

# Drop db

docker-compose exec db psql -U postgres -d postgres -c "DROP DATABASE app"
