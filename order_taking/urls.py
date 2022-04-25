from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),    #sets up the path
    path('update_starter<table_number>',views.update_starter, name='update_starter' ),
    path('update_main<table_number>',views.update_main, name='update_main' ),
    path('update_desert<table_number>',views.update_desert, name='update_desert' )

    #path('<int:order_id>/', views.detail, name='detail')
]