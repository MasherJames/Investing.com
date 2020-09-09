#  kicks off tasks at regular intervals
celery -A app.celery.worker:celery beat --loglevel=info