from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_view, name='landing'),
    path('store/<str:unique_id>/', views.store, name='store'),
]