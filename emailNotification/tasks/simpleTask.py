from celery import shared_task


@shared_task
def add(a,b):
    return a+b

@shared_task
def average(a: list):
    return sum(a)/len(a)

@shared_task
def sum(a: list):
    return sum(a)