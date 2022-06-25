import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testApi.settings')

app = Celery('testApi')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'action_every_minute': {
        'task': 'testApi.tasks.get_data',
        'schedule': crontab()
    },
}
