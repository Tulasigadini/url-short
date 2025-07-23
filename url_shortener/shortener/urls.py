from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps '' to index view
    path('<str:short_code>/', views.redirect_url, name='redirect'),
]