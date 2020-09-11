from celery.schedules import crontab

from app import create_app
from app.celery import make_celery
from app.entities.safaricom import triggerScrapParsePersist

app = create_app()
celery = make_celery(app)


# send signal after app has prepared the configuration.
@celery.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # add entry to the beat scheduler
    sender.add_periodic_task(
        crontab(hour=0, minute=0, day_of_week=1), triggerScrapParsePersist)
