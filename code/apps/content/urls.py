
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('books/<int:pk>', views.detail_book, name='detail-book'),
    path('create_book/', views.create_book, name='create-book'),
    path('books/update/<int:pk>', views.update_book, name='update-book'),
    path('books/delete/<int:pk>', views.delete_book, name='delete-book'),
]