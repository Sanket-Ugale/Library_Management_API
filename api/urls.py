from django.urls import path
import api.views as views

urlpatterns = [
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    path('register/', views.Register.as_view()),
    path('books/', views.BookList.as_view()),
    path('books/<isbn>/', views.BookDetail.as_view()),
]
