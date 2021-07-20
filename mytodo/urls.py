from django.urls import path
from . import views
urlpatterns=[
    path("",views.index),
    path("update_todo/<str:pk>",views.update_tod ,name="update_todo"),
    path("delete_todo/<str:pk>",views.delete_todo,name="delete_todo"),
]