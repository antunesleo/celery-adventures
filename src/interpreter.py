def what_was_said(task_name, excption):
    if task_name == 'add':
        if isinstance(excption, TypeError):
            print('I know what happened, you need to pass to numbers. Cant add, wrong type buddy!')
    if task_name == 'mul':
        if isinstance(excption, TypeError):
            print('I know what happened, you need to pass to numbers. Cant multiply, wrong type buddy!')
