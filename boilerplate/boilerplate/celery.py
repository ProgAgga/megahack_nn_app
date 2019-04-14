import os

from celery import Celery

from boilerplate import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boilerplate.settings')

app = Celery('celery')
app.config_from_object(settings, namespace='CELERY')

# celery worker -A boilerplate
