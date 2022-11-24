
Live demo: https://buyit.161e.tk

### Example endpoints:

- https://buyit.161e.tk/admin - Admin panel
- https://buyit.161e.tk/item/3 - Item info
- https://buyit.161e.tk/order/1 - Order info

## Installation

### Run in Docker

1. Clone this repo `git clone https://github.com/air17/buyit.git` and go to it's root folder.
2. Rename `.env.template` file in the root folder to `.env` and fill it in.
3. Run `docker compose up -d`
4. Optional: create admin user with a command `docker exec -it web python manage.py createsuperuser`
5. Go to http://localhost:8000

### Install for development

0. Install `python3`
1. Clone this repo `git clone https://github.com/air17/chatalyze.git` and go to it's root directory.
2. Install dependencies: `pip install -r requirements.txt` and `pip install -r requirements-dev.txt`
3. Run `pre-commit install` and `pre-commit install --hook-type pre-push` to set up Git hooks
4. Setup PostgreSQL Database
5. Rename `.env.template` to `.env` in `chatalyze/config` directory and fill it in.
6. Run `python manage.py makemigrations`
7. Run `python manage.py migrate`
8. Run `python manage.py runserver`
9. Go to http://127.0.0.1:8000
