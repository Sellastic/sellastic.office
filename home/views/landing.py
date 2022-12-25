from django.shortcuts import render
from django.conf import settings


def landing_view(request):
    context = {
        'page_title': settings.HOME_APP_TITLE,
        'version': settings.VERSION,
    }
    return render(request, "home/landing.html", context)
