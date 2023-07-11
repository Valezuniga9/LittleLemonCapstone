from django.test import TestCase
from restaurant.models import Menu
from test_models import MenuItemTest
from restaurant.serializers import MenuSerializer



class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=9.99, inventory=9)
        self.menu2 = Menu.objects.create(title="Burger", price=5.99, inventory=11)
        self.menu3 = Menu.objects.create(title="Salad", price=7.99, inventory=5)

    def test_getall(self):
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        response = self.client.get('restaurant/menu')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)