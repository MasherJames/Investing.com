web: gunicorn run:app --bind 0.0.0.0:8000
beat: celery -A app.celery.worker:celery beat --loglevel=info
worker: celery -A app.celery.worker:celery worker --loglevel=info
