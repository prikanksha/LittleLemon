from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
      # Add test instances
      Menu.objects.create(title="Pizza", price=9.99, inventory=30)
      Menu.objects.create(title="Burger", price=6.99, inventory=20)
      Menu.objects.create(title="Pasta", price=8.99, inventory=10)

    def test_getall(self):
      menu = Menu.objects.all()
      self.assertEqual(str(list(menu)), '[<Menu: Pizza : 9.99>, <Menu: Burger : 6.99>, <Menu: Pasta : 8.99>]')

