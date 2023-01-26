from django.shortcuts import render
from emailNotification.tasks.emailSender import add
# Create your views here.
add.apply_async(1,2)