from src.interpreter import what_was_said
from celery import Celery

app = Celery('tasks', broker='pyamqp://leonardo:indev107@localhost:5672/celery-adventures',
                      backend='redis://localhost/15')


class MyTask(app.Task):

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        what_was_said(self.name, exc)


@app.task(base=MyTask, name='add')
def add(x, y):
    return x + y


@app.task(base=MyTask, name='mul')
def mul(x, y):
    return x + y


@app.task(base=MyTask, name='long_heavy_task')
def long_heavy_task():
    items = ['qwr', 'ali', 'aap', 'aoi', 'ehu']
    for index in range(0, 15):
        items += (items)

    for item in items:
        print('-------------------------------')
        print('this is the current item', item)

    items.sort()

    items_with_a = []
    for item in items:
        if 'a' in item:
            items_with_a.append(item)


@app.task(base=MyTask, name='trying_to_lock')
def trying_to_lock():
    import time
    for i in range(0, 2500):
        txt = open("/home/leonardo/Documents/task.txt", "a")
        for j in range(0, 500):
            txt.write('{}'.format(time.time()))
        txt.close()
