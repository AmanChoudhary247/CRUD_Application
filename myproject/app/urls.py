from django.urls import path
from . import views


urlpatterns = [
    path("",views.index),
    path("register/",views.register),
    path("table/",views.data),
    path("delete/<int:pk>/",views.user_delete, name="delete"),
    path("update/<int:uid>/",views.update_user, name="update"),
    path("update_view/",views.update_view)
   
   

    
    
]