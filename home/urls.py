from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('store/<str:unique_id>/', views.store, name='store'),
    ]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
