# run celery without docker

celery -A app.celery:celery beat --loglevel=info