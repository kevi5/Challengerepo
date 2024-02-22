from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('books/', views.getbooks, name= "get books"),
    path('addbook/<str:book_name>/', views.addbook, name= "add book"),
    path('members/', views.getmembers, name= "get members"),
    path('addmember/<str:member_name>/', views.addmember, name= "add member"),
    path('checkoutbook/<str:book_id>/<str:member_id>/', views.checkoutbook, name= "checkout"),
    path('returnbook/<str:member_id>/', views.returnbook, name= "return"),
]
