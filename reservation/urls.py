from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import ShowRoomsApiView ,ShowFinishedReservationsApiView ,ShowReservationsApiView

router = DefaultRouter()

router.register('rooms',ShowRoomsApiView , basename='room-list')
router.register('finished_reservations',ShowFinishedReservationsApiView , basename='finished_reservations')
router.register('reservations',ShowReservationsApiView , basename='reservations')


urlpatterns = [
    path('', include(router.urls)),
]