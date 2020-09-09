# worker nodes in the cluster that execute task.
celery -A app.celery.worker:celery worker --loglevel=info