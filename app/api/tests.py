from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

#from api.serializers import ProductSerializer
from shop.models import Product


class ProductApiTests(APITestCase):

    def test_create_product(self):
        """
        Ensure we can create a new product object.
        """
        url = reverse('api/products')
        data = {
            "title": "Test Product",
            "image": "http://localhost:8000/mediafiles/phs1_9NdtHi1.jpg",
            "price": 49.99,
            "status": 2,}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().title, 'Test Product')


"""
{
    "title": "Test Product",
    "image": "http://localhost:8000/mediafiles/phs1_9NdtHi1.jpg", ??Shit does not jet work!!
    "price": 49.99,
    "status": 2
}
"""
