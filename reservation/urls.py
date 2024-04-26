from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ShowRoomsApiView

router = DefaultRouter()

router.register('rooms',ShowRoomsApiView , basename='rooms')

urlpatterns = [
    path('', include(router.urls)),
]