from django.urls import path 
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('computer_entry/', views.computer_entry, name='computer_entry'),
    path('computer_list/', views.computer_list, name ='computer_list'),
    path('computer_edit/<str:pk>/', views.computer_edit, name = 'computer_edit'),
    # path(r'^computer_list/(?P<id>\d+)/$', 'djangoapp.views.computer_edit', name='computer_edit'),
    path('delete/<str:pk>/', views.delete, name = 'delete'),
]
