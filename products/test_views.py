import pytest
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.http import Http404
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware 
from unittest.mock import MagicMock
from .models import Homepage, Product, Category, Group, Rating
from .views import product_detail


class TestHomePage(TestCase):
    """Tests home_page(request)"""
    def test_home_page_success(self):
        """Tests the home page loads successfully with an active homepage"""
        self.active_page = Homepage.objects.create(is_active=True)
        self.not_active_page = Homepage.objects.create(is_active=False)
        url = reverse('products:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['homepage'], self.active_page)

    def test_home_page_no_active_page(self):
        """Tests home_page when no activehomepage exists"""
        url = reverse('products:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.context['homepage'])

    def test_home_page_many_active_pages(self):
        """Tests the view only returns the first active page."""
        self.first_active_page = Homepage.objects.create(is_active=True)
        self.second_active_page = Homepage.objects.create(is_active=True)
        url = reverse('products:home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['homepage'], self.first_active_page)
        

class TestAllProducts(TestCase):
    """Tests all_products(request) view."""
    def test_all_products_empty(self):
        """Tests the page loads when there are no products"""
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 0)
        
    def test_all_products_first_page_pagination(self):
        """Test that the first page displays 8 items."""
        category = Category.objects.create(name="Things", slug="things")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 8)
        self.assertTrue(response.context['products_page'].has_next())
        self.assertFalse(response.context['products_page'].has_previous())
                        
        
    def test_all_products_next_page(self):
        """Tests next page will load page 2"""
        category = Category.objects.create(name="Things", slug="things")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 2)
        self.assertFalse(response.context['products_page'].has_next())
        self.assertTrue(response.context['products_page'].has_previous())
        
    def test_all_products_invalid_page(self):
        """Tests messing up the url defalts back to page 1"""
        category = Category.objects.create(name="Things", slug="things")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 'rubbish'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products_page'].number, 1)
        
                
class TestPlushes(TestCase):
    """Tests plushes(request) view."""
    def test_plushes_empty(self):
        """Tests the page loads when there are no products"""
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 0)
        
    def test_plushes_first_page_pagination(self):
        """Test that the first page displays 8 items."""
        category = Category.objects.create(name="Things", slug="plushes")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 8)
        self.assertTrue(response.context['products_page'].has_next())
        self.assertFalse(response.context['products_page'].has_previous())
                        
        
    def test_plushes_next_page(self):
        """Tests next page will load page 2"""
        category = Category.objects.create(name="Things", slug="plushes")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 2)
        self.assertFalse(response.context['products_page'].has_next())
        self.assertTrue(response.context['products_page'].has_previous())
        
    def test_plushes_invalid_page(self):
        """Tests messing up the url defalts back to page 1"""
        category = Category.objects.create(name="Things", slug="plushes")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 'rubbish'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products_page'].number, 1)
        
class TestPrints(TestCase):
    """Tests prints(request) view."""
    def test_prints_empty(self):
        """Tests the page loads when there are no products"""
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 0)
        
    def test_prints_first_page_pagination(self):
        """Test that the first page displays 8 items."""
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 8)
        self.assertTrue(response.context['products_page'].has_next())
        self.assertFalse(response.context['products_page'].has_previous())
                        
        
    def test_prints_next_page(self):
        """Tests next page will load page 2"""
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['products_page']), 2)
        self.assertFalse(response.context['products_page'].has_next())
        self.assertTrue(response.context['products_page'].has_previous())
        
    def test_prints_invalid_page(self):
        """Tests messing up the url defalts back to page 1"""
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small")
        for i in range(10):
            Product.objects.create(name=f"Product {i}", price=10.00, group=group, slug=f"procuct{i}")
        url = reverse('products:allproducts')
        response = self.client.get(url, {'page': 'rubbish'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['products_page'].number, 1)
        
        
class TestProductDetail(TestCase):
    """Tests product_detail view and sets url"""
    def setUp(self):
        """Create a product."""
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small")
       
        self.product = Product.objects.create(name="product", slug='product', price=10.00, group=group, code="TESTCODE")
        self.url = reverse('products:productdetail', kwargs={'slug': self.product.slug})
        
    def test_product_detail_success(self):
        """Tests product_detail renders when a GET request is passed. Checks rating_average is calculeted."""
        Rating.objects.create(product=self.product, rating=4)
        Rating.objects.create(product=self.product, rating=5)
        
        response = self.client.get(self.url) 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['product'], self.product)
        self.assertEqual(response.context['rating_average'], 4.5)
        
    def test_product_detail_no_rating(self):
        """Tests view handles products with no ratings."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['rating_average'], 0)
        
    def test_product_detail_pagination(self):
        """Tests paginator shows 4 items per page."""
        for i in range(6):
            Rating.objects.create(product=self.product, rating=4)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['ratings_page']), 4)
        self.assertTrue(response.context['ratings_page'].has_next())
        self.assertFalse(response.context['ratings_page'].has_previous())
        
    def test_product_detail_page_2(self):
        """Tests ratings in page 2"""
        for i in range(6):
            Rating.objects.create(product=self.product, rating=4)
        response = self.client.get(self.url, {'page': 2})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['ratings_page']), 2)
        self.assertFalse(response.context['ratings_page'].has_next())
        self.assertTrue(response.context['ratings_page'].has_previous())
    
    def test_product_detail_404(self):
        """Tests view returns 404 if product slug does not exist."""
        invalid_url = reverse('products:productdetail', kwargs={'slug': 'no-slug'})
        response = self.client.get(invalid_url)
        self.assertEqual(response.status_code, 404)
        
class TestRateProduct(TestCase):
    def setUp(self):
        """Creates product and user. Sets url."""
        self.client = Client()
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small") 
        self.product = Product.objects.create(name="product", slug='product', price=10.00, group=group, code="TESTCODE")
        self.user = User.objects.create_user(username='testuser', password='password')
        self.url = reverse('products:rateproduct', kwargs={'slug': self.product.slug})
    
    def test_rate_product_get(self):
        """Tests page loads the rating form."""   
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/rate_product.html")
        self.assertIn('rating_form', response.context)
        self.assertEqual(response.context['product'], self.product)
            
        
class TestUpdateReview(TestCase):
    def setUp(self):
        """ Creates products and users. Creates rating. Sets url"""   
        category = Category.objects.create(name="Things", slug="3d-prints")
        group = Group.objects.create(name="small", category=category, slug="small")
        self.product = Product.objects.create(name="product", slug='product', price=10.00, group=group, code="TESTCODE")
        self.owner = User.objects.create_user(username="owner", password="password2")
        self.non_owner = User.objects.create_user(username="non_user", password='password1')
        self.rating = Rating.objects.create(product=self.product, user=self.owner, rating='3', title='ok', comment='Its ok')           
        self.url = reverse('products:updatereview', kwargs={'id': self.rating.id})
    
    def test_update_review_get_request(self):
        """Tests get request loads the page and populates the form instance"""
        self.client.login(username="owner", password="password2")
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/update_review.html")
        self.assertEqual(response.context['rating'], self.rating)
        self.assertIn('rating_form', response.context)
    
    def test_update_review_permission_denied(self):
        """Tests non owner user cannot update the rating"""
        self.client.login(username='non_user', password='password1')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 403)
                          
        
        
        
        
        
    
        
        
        
        
        
          
        
                        
            
    
        







