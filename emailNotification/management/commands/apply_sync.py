from django.core.management.base import BaseCommand
from emailNotification.tasks.simpleTask import add

class Command(BaseCommand):
    help = "run with apply_async"

    def handle(self, *args, **options):
        r = add.apply_async([1, 2])
        # r = add.apply_async([1, 2], queue=queue1) # we can pass queue to apply_async

        print(r) # return just task Id
        # print(r.get()) #for get value
        # print(r.get(timeout=10, propagat=True)) # propagat return Errors when it was False just return str of error
        # r.forget() # if we dont have needed to value and we must forget for free memory

        # print(r.traceback) # for traceback errors
        #print(r.ready())

