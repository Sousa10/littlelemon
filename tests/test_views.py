from django.test import TestCase, Client
from reservation.models import Menu
from reservation.serializers import MenuSerializer
from django.urls import reverse

# initialize the APIClient app
client = Client()

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Cake", price=40, inventory=10)
        Menu.objects.create(title="Candy", price=10, inventory=1000)

    def test_get_all(self):
        # get API response
        response = client.get(reverse('get_menu'))
        response_data = response.json()['results']
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        print(serializer.data)
        self.assertListEqual(response_data, serializer.data)