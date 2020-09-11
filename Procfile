web: gunicorn app:app
celery -A app.celery.worker:celery worker --loglevel=info