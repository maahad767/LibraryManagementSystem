from django.urls import path

from . import views


urlpatterns = [
    path('', views.MainView.as_view(), name='home'),
    path('books/', views.BooksListView.as_view(), name='books'),
]
