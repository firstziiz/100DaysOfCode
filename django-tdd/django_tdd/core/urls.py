from django.urls import path
from core import views

urlpatterns = [
    path('', views.TodoListView.as_view()),
]
