from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:entry_name>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),
    path('create_new/', views.create_entry, name='create_new'),
    path('create/', views.create_entry, name='create'),
    path('edit/<str:entry_name>/', views.edit, name='edit'),
    path('random/', views.random_entry, name='random_entry')
]
