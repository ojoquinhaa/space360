from os import system
def debug(): system("flask --app app.py run --debug")
def migrate(): system("alembic upgrade head")