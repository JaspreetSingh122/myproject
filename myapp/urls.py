from django.urls import path,include
from . import views
urlpatterns = [
    path('about/', views.myfunc,name='Login'),
    path('', views.myfunc2,name='Home')
   
]
