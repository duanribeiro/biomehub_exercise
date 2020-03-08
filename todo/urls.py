from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from todoapp.views import ToDoViewSet, TaskViewSet


router = routers.DefaultRouter()
router.register(r'todo', ToDoViewSet)
router.register(r'task', TaskViewSet)


urlpatterns = [
    path(r'', include(router.urls)),
    path('admin/', admin.site.urls),
]


