web: gunicorn run:app
beat: celery -A app.celery.worker:celery beat --loglevel=info
worker: celery -A app.celery.worker:celery worker --loglevel=info
