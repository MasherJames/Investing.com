web: gunicorn app:app
worker: celery -A app.celery.worker:celery worker --loglevel=info
worker: celery -A app.celery.worker:celery beat --loglevel=info