from django.shortcuts import render
from django.http import HttpResponse

# This is the simplest way to call a view for Django application, which would be link to
# a URL.
#


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
