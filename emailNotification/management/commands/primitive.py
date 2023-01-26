from django.core.management.base import BaseCommand
from emailNotification.tasks.simpleTask import add, average
from celery import group, chain, chord


class Command(BaseCommand):
    help = "run with primitive "
    """
    Group 
    Chain 
    Chord
    """

    def handle(self, *args, **options):
        # """ Group """
        # g = group(add.s(i, i) for i in range(10))
        # print(g().get())
        #
        # "partial group"
        # g = group(add.s(i) for i in range(10))
        # print(g(10).get())
        #
        #################################################
        # """ Chain """
        # ch = chain(add.s(2, 6) | add.s(6))
        # # or
        # ch = (add.s(2, 6) | add.s(6))
        # print(ch().get())

        # "partial chain"
        # ch = (add.s(2,) | add.s(6))
        # print(ch(7).get())
        #
        ###################################################
        """ Chord """
        #
        # ch = chord((add.s(i, i) for i in range(10)), average.s())
        # # or
        # ch = (group(add.s(i, i) for i in range(10)) | average.s())
        # print(ch().get())
