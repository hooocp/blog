from django.shortcuts import render
from django.conf import settings


def global_default_settings(request):
    return {'my_name': settings.MY_NAME, }


# Create your views here.
def index(request):
    return render(request, 'index.html', locals())
