from django.urls import path,include
from . import views
urlpatterns = [
    path('Login/', views.myfunc,name='Login'),
    path('Home/', views.myfunc2,name='Home')
   
]
