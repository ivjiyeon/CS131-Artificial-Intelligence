import unittest
from shopSmart import shopSmart
from shop import FruitShop


class TestShopSmart(unittest.TestCase):

    def test_shop_smart_1(self):
        orders = [('apples', 1.0), ('oranges', 3.0)]

        dir1 = {'apples': 2.0, 'oranges': 1.0}
        shop1 = FruitShop('shop1', dir1)

        dir2 = {'apples': 1.0, 'oranges': 5.0}
        shop2 = FruitShop('shop2', dir2)

        shops = [shop1, shop2]

        self.assertEqual(shopSmart(orders, shops).getName(), "shop1")
    
    def test_shop_smart_2(self):
        orders = [('apples', 3.0)]

        dir1 = {'apples': 2.0, 'oranges': 1.0}
        shop1 = FruitShop('shop1', dir1)

        dir2 = {'apples': 1.0, 'oranges': 5.0}
        shop2 = FruitShop('shop2', dir2)

        shops = [shop1, shop2]

        self.assertEqual(shopSmart(orders, shops).getName(), "shop2")

    def test_shop_smart_3(self):
        dir1 = {'apples': 2.0, 'oranges':1.0}
        shop1 = FruitShop('shop1',dir1)

        dir2 = {'apples': 1.0, 'oranges': 5.0}
        shop2 = FruitShop('shop2',dir2)

        dir3 = {'apples': 1.5, 'oranges': 2.0}
        shop3 = FruitShop('shop3',dir3)

        shops = [shop1, shop2, shop3]

        order = [('apples',10.0), ('oranges',3.0)]

        self.assertEqual(shopSmart(order, shops).getName(), "shop3")