from django.contrib.messages import get_messages
from django.shortcuts import render


def error_page(request):
    """ Collect all django messages and show it to user """
    return render(request, 'error.html', {'messages': get_messages(request)})
