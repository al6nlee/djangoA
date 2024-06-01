from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # 书
    path('books/', views.BookView.as_view()),
    path('books/<int:pk>', views.BookViewDetail.as_view()),

    # 作者
    path('authors/', views.AuthorView.as_view()),
    path('authors/<int:pk>', views.AuthorViewDetail.as_view()),

    # 作者详情
    path('authorsdetail/', views.AuthorDetailView.as_view()),
    path('authorsdetail/<int:pk>', views.OneAuthorViewDetail.as_view()),

    # 出版社
    path('publish/', views.PublishView.as_view()),
    path('publishdetail/<int:pk>', views.PublishViewDetail.as_view()),
]
