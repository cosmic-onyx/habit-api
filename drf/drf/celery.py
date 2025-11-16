import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf.settings')

import django
django.setup()

from celery import Celery

from django.conf import settings


app = Celery("drf")

app.conf.broker_url = settings.CELERY_BROKER_URL
app.conf.result_backend = settings.CELERY_RESULT_BACKEND
app.conf.timezone = settings.TIME_ZONE
app.conf.result_extended = True

app.autodiscover_tasks()

import tasks.habit_task

app.conf.beat_schedule = {
    'select_now_habits_and_send_notify': {
        'task': 'habit_task.select_today_habits',
        'schedule': 60.0,
    }
}
