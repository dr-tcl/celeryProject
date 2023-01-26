from django.core.management.base import BaseCommand
from emailNotification.tasks.simpleTask import add


class Command(BaseCommand):
    help = "run with signature"

    def handle(self, *args, **options):
        # func = add.signature((3, 6), countdown=3)
        # re = func.apply_async()
        # print(re)
        # print(re.get())
        # print(re.forget())

        ###########################################################

        # func = add.signature((3,), countdown=3)
        # re = func.apply_async([5,])
        # print(re)
        # print(re.get())

        ###########################################################

        func = add.s(3,)
        re = func.apply_async([5, ])
        print(re)
        print(re.get())