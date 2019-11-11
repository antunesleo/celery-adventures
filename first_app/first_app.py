from celery_stuff.tasks import serve_a_beer


def start_serve_a_beer():
    serve_a_beer.delay()

start_serve_a_beer()