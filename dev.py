from os import system
def debug(): system("flask --app cam360.app run --debug")
def migrate(): system("alembic upgrade head")