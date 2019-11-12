from celery_stuff.tasks import serve_a_beer # Importing the task


def start_serve_a_beer():
    """ Starts the execution of a celery task with the delay method.
    the delay method doesn't wait the task execution be finished.
    """
    serve_a_beer.delay()
    print('This will be executed before the serve_a_beer task be finished')

start_serve_a_beer()