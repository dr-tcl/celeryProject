from django.core.management.base import BaseCommand
from project.celery import app

class Command(BaseCommand):
    help = "run with async_result"

    def handle(self, *args, **options):

        """
        AsyncResult
        """
        taskId = "c0037c8e-d455-4030-b858-2c624180a8cd"
        res = app.AsyncResult(taskId)
        print(res.successful())
        print(res.failed())
        print(res.state()) # PENDING, STARTED, SUCCESS