from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
  def test_create_menu(self):
    item = Menu.objects.create(title="Pizza", price=17.99, inventory=10)
    print(item)
    self.assertEqual(item.__str__(), "Pizza : 17.99")