from src.tasks import add, mul, long_heavy_task, trying_to_lock, orchestrator_task


def start_add(x, y):
    try:
        zas = add.delay(x, y)
        print('task', zas)
    except Exception as ex:
        print(ex)


def start_mul(x, y):
    try:
        zas = mul.delay(x, y)
        print('task', zas)
    except Exception as ex:
        print(ex)


def start_long_heavy_task():
    for i in range(0, 2000):
        import time
        time.sleep(0.8)
        long_heavy_task.apply_async()


def start_trying_to_lock():
    for i in range(0, 200):
        import time
        time.sleep(0.2)
        try:
            zas = trying_to_lock.delay()
            print('task', zas)
        except Exception as ex:
            print(ex)

def start_orchestrator_task():
    try:
        zas = orchestrator_task.delay(10)
        print('task', zas)
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    start_orchestrator_task()
