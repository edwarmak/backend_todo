from django.urls import path
from . import views

urlpatterns = [
path('api/todo', views.TodoList.as_view(), name='todo_list'), # when you go to api/todo you will be routed to the TodoList view
path('api/todo/<int:pk>', views.TodoDetail.as_view(), name='todo_detail'), # when you go to api/todo you will be routed to the TodoDetail view
]
