from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import ShoppingBasket, ShopItems
from products.models import Product, Category, Group


class TestShoppingBag(TestCase):
    """Test shopping_bag view"""
    def setUp(self):
        """Sets up url. Create user. Create product.
            Create shopping bag and basket items."""
        self.url = reverse('shopping_bag:shoppingbag')
        self.user = User.objects.create_user(
            username='Philip204', password='password1')
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(
            name="small", category=category, slug="small")
        self.product = Product.objects.create(
                                            name="product",
                                            slug='product',
                                            price=10.00,
                                            group=group,
                                            code="TESTCODE"
                                        )
        self.basket = ShoppingBasket.objects.create(user=self.user)
        self.basket_item = ShopItems.objects.create(
                                                basket=self.basket,
                                                product=self.product,
                                                quantity=2
                                            )

    def test_shopping_bag_loads(self):
        """Tests the shopping bag loads successfully
            and shows the shopping items"""
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "shopping_bag/shopping_bag.html")
        context_items = response.context['items']
        self.assertIn(self.basket_item, context_items)
        self.assertEqual(len(context_items), 1)


class TestAddToBag(TestCase):
    """Tests add_to_bag view"""
    def setUp(self):
        """Sets up url. Creates user. Creates product. Creates basket"""
        self.user = User.objects.create_user(
            username='Philip204', password='password1')
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(
            name="small", category=category, slug="small")
        self.product = Product.objects.create(
                                            name="product",
                                            slug='product',
                                            price=10.00,
                                            group=group,
                                            code="TESTCODE"
                                        )
        self.url = reverse('shopping_bag:addtobag',
                           kwargs={'product_code': self.product.code})

    def test_add_to_bag_redirect(self):
        """Tests the view redirects to the original page"""
        self.client.login(username='Philip204', password='password1')
        current_page_url = '/'
        payload = {'quantity': 2, 'redirect_url': current_page_url}
        response = self.client.post(self.url, data=payload)
        self.assertRedirects(response, current_page_url)

    def test_add_to_bag_new_item(self):
        """Tests a new ShopItems record is created when a new product is added"""
        self.client.login(username='Philip204', password='password1')
        payload = {'quantity': 3, 'redirect_url': '/'}
        self.client.post(self.url, data=payload)
        item = ShopItems.objects.get(product=self.product)
        self.assertEqual(item.quantity, 3)


class TestUpdateBag(TestCase):
    """Tests update_bag view"""
    def setUp(self):
        """Create user. Create product. Create basket and add product. Set up url"""
        self.user = User.objects.create_user(
            username='Philip204', password='password1')
        category = Category.objects.create(
            name="Things", slug="3d-prints")
        group = Group.objects.create(
            name="small", category=category, slug="small")
        self.product = Product.objects.create(
                                            name="product",
                                            slug='product',
                                            price=10.00,
                                            group=group,
                                            code="TESTCODE"
                                        )
        self.basket = ShoppingBasket.objects.create(user=self.user)
        self.shop_item = ShopItems.objects.create(
            basket=self.basket, product=self.product, quantity=3)
        self.url = reverse('shopping_bag:updatebag',
                           kwargs={'product_code': self.product.code})

    def test_update_bag_update_quantity(self):
        """Tests the view saves the new quantity"""
        self.client.login(username='Philip204', password='password1')
        current_page_url = '/'
        payload = {'quantity': 5, 'redirect_url': current_page_url}
        response = self.client.post(self.url, data=payload)
        self.assertRedirects(response, current_page_url)
        self.shop_item.refresh_from_db()
        self.assertEqual(self.shop_item.quantity, 5)


class TestRemoveFromBasket(TestCase):
    """Tests remove_from_basket view"""
    def setUp(self):
        """Creates user. Creates product. Creates basket and item. Sets up url"""
        self.user = User.objects.create_user(
            username='Philip204', password='password')
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(
            name="small", category=category, slug="small")
        self.product = Product.objects.create(
                                            name="product",
                                            slug='product',
                                            price=10.00,
                                            group=group,
                                            code="TESTCODE"
                                        )
        self.basket = ShoppingBasket.objects.create(user=self.user)
        self.shop_item = ShopItems.objects.create(
            basket=self.basket, product=self.product, quantity=3)
        self.url = reverse('shopping_bag:removefrombasket',
                           kwargs={'product_code': self.product.code})
