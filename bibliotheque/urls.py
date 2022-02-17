from django.urls import path
from .import views

urlpatterns = [
      path('login/',views.loginPage, name='login'),
      path('register/',views.registerPage, name='register'),
      path('logout/',views.logoutUser, name='logout'),


      path('',views.index, name='index'),
      path('',views.index_ut, name='index_ut'),
      path('user/',views.userPage, name='user-page'),
       
      path('books',views.books, name='books'), 
      path('books_ut',views.books_ut, name='books_ut'),
      path('index_ut/',views.index_ut, name='index_ut'),

      path('update/<int:id>', views.update, name='update'),
      path('delete/<int:id>', views.delete, name='delete'),
     # path('test/', views.test, name='test'),

]

