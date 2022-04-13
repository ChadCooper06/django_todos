from django.urls import path

from . import views, models

urlpatterns = [
    path('', views.index, name='index'),
    path('models/User', models.User, name='user'),
    path('models/Todo', models.Todo, name='todo'),
    path('models/Categories', models.Categories, name='categories'),
    path('models/Events', models.Events, name='events'),
]