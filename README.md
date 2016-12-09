# RestPlaces
Sample DjangoProject + Django Rest framework 

# Create virtual enviroment
pip install virtualenvwrapper-win
mkvirtualenv myproject
workon myproject

# install django and djangorestframework
pip install django
pip install djangorestframework

# Create project
django-admin startproject myproject
cd myproject
python manage.py startapp app

# Set up database and create superuser
python manage.py migrate
python manage.py createsuperuser

# Set djangorestframework in  settings.py
INSTALLED_APPS = (
    'app',
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGE_SIZE': 5
}


Source: http://www.django-rest-framework.org/tutorial/quickstart/
