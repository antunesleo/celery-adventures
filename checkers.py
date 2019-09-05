from src.tasks import app


def check_add(task_id):
    res = app.AsyncResult(task_id)
    print(res)


if __name__ == '__main__':
    check_add('05855afe-d310-4aa0-a455-0135529d8093')
