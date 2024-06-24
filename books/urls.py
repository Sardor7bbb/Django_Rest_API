from django.urls import path

from books.views import BookListAPIView, get_book, update_book, create_book, delete_book

urlpatterns = [
    path('', BookListAPIView.as_view()),
    path('create/', create_book),
    path('<int:pk>/', get_book),
    path('<int:pk>/update/', update_book),
    path('<int:pk>/delete/', delete_book),

]
