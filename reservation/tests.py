from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.utils import timezone
from accounts.models import CustomUser, Team
from reservation.models import Room, Reservation, Comment

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(username='testuser', password='testpass')
        # self.client.login(username='testuser', password='testpass')
        try:
            self.team = Team.objects.create(name='Development Team', leader=self.user)
        except Exception as e:
            print('_________________')
            print('_________________')
            print('_________________')
            print('_________________')
            print('_________________')
            print(e.args)
        self.room1 = Room.objects.create(name='Conference Room A', capacity=10, point=4.5)
        self.room2 = Room.objects.create(name='Conference Room B', capacity=20, point=4.8)

        now = timezone.now()
        self.finished_reservation = Reservation.objects.create(
            room=self.room1,
            team=self.team,
            date=now.date(),
            start=now.time().replace(hour=8),
            end=now.time().replace(hour=9)
        )

        self.upcoming_reservation = Reservation.objects.create(
            room=self.room2,
            team=self.team,
            date=now.date(),
            start=now.time().replace(hour=10),
            end=now.time().replace(hour=11)
        )

        self.comment1 = Comment.objects.create(
            reservation=self.finished_reservation,
            text="Great room!",
            point=4
        )
class ShowRoomsApiViewTest(APITestCase):
    def test_list_rooms(self):
        response = self.client.get(reverse('room-list-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)
        self.assertEqual(response.data['results'][0]['name'], 'Conference Room A')

    def test_search_rooms(self):
        response = self.client.get(reverse('room-list-list'), {'search': 'Conference Room A'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'Conference Room A')

    def test_order_rooms_by_capacity(self):
        response = self.client.get(reverse('room-list-list'), {'ordering': 'capacity'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'Conference Room A')
