from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    #sets up the path
    #path('<int:order_id>/', views.detail, name='detail')
]