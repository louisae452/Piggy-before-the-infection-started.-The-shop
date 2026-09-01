from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from checkout.models import Order, OrderLineItem
from products.models import Category, Group, Product
from .models import Profile


class TestProfile(TestCase):
    """ Tests profile view"""
    def setUp(self):
        """Creates user and profile
            Sets url"""
        self.client = Client()
        self.url = reverse('profiles:profile')
        self.user = User.objects.create_user(
                                            username='Philip204',
                                            password='password1',
                                            email='philip@example.com',
                                            first_name='Philip',
                                            last_name='Marlow'
                                        )
        self.profile, created = Profile.objects.get_or_create(user=self.user)
        self.profile.phone_number = '0987876546',
        self.profile.street_address1 = '24 Pine Road'
        self.profile.town = 'Lucella'
        self.profile.postcode = 'LU1 3PM'
        self.profile.save()

    def test_profile_requires_login(self):
        """Tests unathenticated users are redirected to the login screen"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_profile_user(self):
        """Tests an authenticated user can access the page and
            forms are loaded"""
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertIn('userform', response.context)
        self.assertIn('profileform', response.context)
        self.assertIn('emailform', response.context)

    def test_profile_personal_save(self):
        """Tests personal information is saved"""
        self.client.login(username='Philip204', password='password1')
        post_data = {
            'personalreset': '',
            'first_name': 'Luis Felipe',
            'last_name': 'Hernandez'
        }
        response = self.client.post(self.url, data=post_data)
        self.assertRedirects(response, self.url)
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'Luis Felipe')
        self.assertEqual(self.user.last_name, 'Hernandez')

    def test_profile_shipping_save(self):
        """Tests shipping info is saved"""
        self.client.login(username='Philip204', password='password1')
        post_data = {
                'shippingreset': '',
                'phone_number': '10101010',
                'street_address1': '3 Mapple Avenue',
                'town': 'Doveport',
                'postcode': 'DO6 1PN'
            }
        response = self.client.post(self.url, data=post_data)
        self.assertRedirects(response, self.url)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.phone_number, '10101010')
        self.assertEqual(self.profile.street_address1, '3 Mapple Avenue')
        self.assertEqual(self.profile.town, 'Doveport')
        self.assertEqual(self.profile.postcode, 'DO6 1PN')


class TestOrderHistory(TestCase):
    """Tests order_history"""
    def setUp(self):
        """Sets up url. Sets up users. Sets up order"""
        self.client = Client()
        self.user1 = User.objects.create_user(
                                            id=101,
                                            username='Philip204',
                                            password='password1'
                                        )
        self.user2 = User.objects.create_user(
                                            id=102,
                                            username='Florencio32',
                                            password='password2'
                                        )
        self.url_user1 = reverse(
                                'profiles:orderhistory',
                                kwargs={'user_id': self.user1.id}
                            )
        self.order_user1_old = Order.objects.create(
                                                user=self.user1,
                                                street_address1='23 Pine Road',
                                                town='Lucella',
                                                postcode='LU3 9PH',
                                                email='philip@example.com'
                                            )
        self.order_user1_old.date = '2025-07-10'
        self.order_user1_old.save()
        self.order_user1_new = Order.objects.create(
                                                user=self.user1,
                                                street_address1='23 Pine Road',
                                                town='Lucella',
                                                postcode='LU3 9PH',
                                                email='philip@example.com'
                                            )
        self.order_user2 = Order.objects.create(
                                            user=self.user2,
                                            street_address1='24 Mapple Avenue',
                                            town='Lucella',
                                            postcode='LU3 9PH',
                                            email='philip@example.com'
                                        )

    def test_order_history_requires_login(self):
        """Tests order_history requires login"""
        response = self.client.get(self.url_user1)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_order_history_success(self):
        """Tests logged in users get a list of their orders
            from newest to oldest"""
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.url_user1)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/order_history.html")
        orders_in_context = list(response.context['order_list'])
        self.assertIn(self.order_user1_new, orders_in_context)
        self.assertIn(self.order_user1_old, orders_in_context)
        self.assertNotIn(self.order_user2, orders_in_context)
        self.assertEqual(orders_in_context[0], self.order_user1_new)
        self.assertEqual(orders_in_context[1], self.order_user1_old)


class TestPastOrderDetail(TestCase):
    """Tests past_order_detail"""
    def setUp(self):
        """Sets url.
            Creates user
            Creates product"""
        self.client = Client()
        self.user_1 = User.objects.create_user(
                                            username='Philip204',
                                            password='password1'
                                        )
        self.user_2 = User.objects.create_user(
                                            username='Florencio32',
                                            password='password2'
                                            )
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(
                                    name="small",
                                    category=category,
                                    slug="small"
                                )
        self.product = Product.objects.create(
                                        name="product",
                                        slug='product',
                                        price=10.00,
                                        group=group,
                                        code="TESTCODE"
                                    )
        self.user1_order = Order.objects.create(
            user=self.user_1,
            email='philiop@example.com',
            grand_total=20.00,
            full_name='Philip Marlow')
        self.line_item = OrderLineItem.objects.create(
            order=self.user1_order,
            product=self.product,
            quantity=1,
            lineitem_total=20.00
        )
        self.guest_order = Order.objects.create(
            user=None,
            email='guest@example.com',
            grand_total=10.00,
            full_name='Peter Smith')
        self.user1_url = reverse(
            'profiles:pastorderdetail',
            kwargs={'order_id': self.user1_order.id}
        )
        self.guest_url = reverse(
            'profiles:pastorderdetail',
            kwargs={'order_id': self.guest_order.id}
        )
        self.invalid_order_url = reverse(
                                         'profiles:pastorderdetail',
                                         kwargs={'order_id': 999}
                                         )

    def test_past_order_detail_requires_login(self):
        """Tests past_order_detail requires login"""
        response = self.client.get(self.user1_url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_past_order_detail_success(self):
        """Tests that the order owner can view the order"""
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.user1_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/past_order_detail.html")
        self.assertEqual(response.context['order'], self.user1_order)
        self.assertIn(self.line_item, response.context['order_items'])

    def test_past_order_detail_non_owner(self):
        """Tests that a user cannot access somebody else's order"""
        self.client.login(username='Florencio32', password='password2')
        response = self.client.get(self.user1_url)
        self.assertEqual(response.status_code, 403)

    def test_past_order_detail_guest_order(self):
        """Tests that a user cannot access a guest order"""
        self.client.login(username='Philip204', password='password1')
        response = self.client.get(self.guest_url)
        self.assertEqual(response.status_code, 403)

    def test_past_order_detail_non_order(self):
        """Test a non exiting order throws a 404 error"""
        self.client.login(username='philip204', password='password1')
        response = self.client.get(self.invalid_order_url)
        self.assertEqual(response.status_code, 404)
