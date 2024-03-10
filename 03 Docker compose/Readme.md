# Django Application Docker Setup

This repository contains a Django application Docker setup with PostgreSQL using Docker Compose.

## Prerequisites
- Docker: Ensure Docker is installed on your machine. If not, you can download and install it from [https://www.docker.com/get-started](https://www.docker.com/get-started).

## Getting Started

### 1. Clone the Repository
```bash
git clone <repository_url>
cd <repository_directory>
```

### 2. Create a Django Project
If you haven't created a Django project yet, you can do so with the following command:
```bash
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
```

### 3. Update Django Settings
In the `settings.py` file of your Django project, configure the database settings to use environment variables:
```python
import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'mydb'),
        'USER': os.environ.get('POSTGRES_USER', 'myuser'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'mypassword'),
        'HOST': 'db',
        'PORT': '5432',
    }
}
```

### 4. Docker Compose Setup
Create a `docker-compose.yml` file in the root of your Django project with the following content:

```yaml
version: '3'

services:
  db:
    image: postgres:12
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword

  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - db
```

### 5. Build and Run
Run the following command to build and run your Django application with Docker Compose:
```bash
docker-compose up --build
```

### 6. Access the Application
Once the containers are running, you can access your Django application at:
[http://localhost:8000](http://localhost:8000)



### More Commands

- To stop the containers:
  ```bash
  docker-compose down
  ```

- To access the Django app's shell:
  ```bash
  docker-compose exec web python manage.py shell
  ```

- To run Django migrations:
  ```bash
  docker-compose exec web python manage.py migrate
  ```

- To create a new Django app inside the container:
  ```bash
  docker-compose exec web python manage.py startapp <app_name>
  ```

- To create a superuser for Django admin:
  ```bash
  docker-compose exec web python manage.py createsuperuser
  ```

- To view logs of running containers:
  ```bash
  docker-compose logs
  ```

- To view running containers:
  ```bash
  docker-compose ps
  ```

- To access the PostgreSQL database shell:
  ```bash
  docker-compose exec db psql -U myuser -d mydb
  ```

- To list all Docker volumes:
  ```bash
  docker volume ls
  ```

- To remove all Docker volumes (use with caution):
  ```bash
  docker volume prune
  ```



## Additional Notes

- Make sure your Django app is configured to allow connections from `localhost` for development purposes.
- For production, consider using a separate `docker-compose.prod.yml` file with additional configurations like using `gunicorn` instead of Django's development server, a separate Dockerfile optimized for production, and possibly a reverse proxy like Nginx.
- Remember to secure your sensitive data (like database credentials) in production environments.

This setup provides a basic Dockerized Django application with a PostgreSQL database. Adjustments can be made based on your specific requirements or preferences.
