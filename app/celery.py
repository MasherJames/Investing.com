
import os
from celery import Celery
from . import create_app

app = create_app()


celery = Celery(app.name, broker=os.getenv("CELERY_BROKER_URL"))
# disable UTC so that Celery can use local time
celery.conf.enable_utc = False

if __name__ == '__main__':
    celery.start()
