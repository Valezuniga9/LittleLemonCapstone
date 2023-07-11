from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest (TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='Ice Cream', price= 8.00, inventory= 8)
        self.assertEqual(item, 'Ice Cream: 8.00')

    