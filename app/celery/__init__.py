from celery import Celery

'''
 - create a new Celery object
 - configure the broker
 - update the rest of the Celery config
 - create a subclass of the task and wrap the task execution in an application context.
'''


def make_celery(app):
    # create a celery instance with the message broker url
    celery = Celery(
        app.import_name, backend=app.config['CELERY_RESULT_BACKEND'], broker=app.config["REDIS_URL"])

    # subclass tasks and hook up the app context
    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)
    celery.Task = ContextTask
    return celery
