from src.interpreter import what_was_said
from celery import Celery

app = Celery('celery_stuff', broker='redis://localhost/2')


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


@app.task(base=MyTask, name='orchestrator_task')
def orchestrator_task(task_nu):
    print('STARTING TO RUN ALL THE {} TASKS'.format(task_nu))
    for i in range(0, task_nu):
        print('---------------------------------------')
        orchestrated_task.apply((i,))
    print('FINISHED ALL THE TASKS')


@app.task(base=MyTask, name='orchestrated_task')
def orchestrated_task(task_number):
    import time
    import random
    print('I AM EXECUTING TASK {} '.format(task_number))
    time.sleep(random.randint(1, 4))
    print('FINISHED TASK {}'.format(task_number))
