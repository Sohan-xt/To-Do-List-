from django.urls import path
from . import views
urlpatterns = [
    path('home',views.home),
    path('about',views.about),
    path('index/home',views.home),

    path('registrations',views.registrations),
    path('signup',views.signup),

    path('login',views.login),
    path('log', views.log, name='login'),

    path('show',views.show),  
    path('del/<int:id>',views.delete), 
    path('edit/<int:id>',views.edit),
    path('editcode/<int:id>',views.editcode),  
    path('todo',views.todo),

    path('tododata',views.tododata),
    path('adddata',views.adddata),
]