import os
from celery import Celery



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'robot.settings')

app = Celery('robot', include=['user.tasks'])

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'print_users_count_every_minute': {
        'task': 'user.tasks.print_users_count',
        'schedule': 60,
        'args': (),
        'kwargs': {},
    },
}

app.conf.timezone = 'UTC'

