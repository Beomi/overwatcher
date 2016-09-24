# django core modules
from django.shortcuts import render
from django.http import JsonResponse

# Custorm core modules
from core.views import _get_overwatch_tech


def index(request):
    return render(request, 'servers/index.html')


def server_status(request):
    pass