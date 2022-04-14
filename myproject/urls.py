"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myproject import settings
from rest_framework import routers
from todo_list.views import UserViewSet, TodoViewSet, CategoriesViewSet, EventsViewSet
from todo_list.models import User, Todo, Categories, Events

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'todo',TodoViewSet)
router.register(r'categories', CategoriesViewSet)
router.register(r'events', EventsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('todo_list/', include('todo_list.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]



