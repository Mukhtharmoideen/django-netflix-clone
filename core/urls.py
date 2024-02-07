from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('movie/<str:pk>', views.movie, name='movie'),
    path('genre/<str:pk>/', views.genre, name='genre'),
    path('my_list', views.my_list, name='my_list'),
    path('add-to=list', views.add_to_list, name='add-to-list'),
    path('search', views.search, name='search')
    
]