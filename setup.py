from setuptools import setup, find_packages
setup(
    name='space360',
    version='1.0.0',
    author='ojoquinhaa',
    author_email='jlpradoneiva@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'SQLAlchemy',
        'python-dotenv',
        'Flask_SQLAlchemy',
        'pymysql',
        'alembic',
        'Pillow',
        'mysql-connector-python',
        'cryptography'    
    ],
    entry_points={
        'console_scripts': [
            'debug=dev:debug',
            'migrate=dev:migrate'
        ]
    }
)