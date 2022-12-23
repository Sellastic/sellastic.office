from django.http import HttpResponse


def landing_view(request):
    return HttpResponse("Sellastic Office Temp Landing Page")