from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer

from shop.models import Product

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/product-list/',
		'Detail View':'/product-detail/<str:pk>/',
		'Create':'/product-create/',
		'Update':'/product-update/<str:pk>/',
		'Delete':'/product-delete/<str:pk>/',}

	return Response(api_urls) # JsonResponse

@api_view(['GET'])
def productList(request):
	products = Product.objects.all()
	serializer = ProductSerializer(products, many=True)

	return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
	product = Product.objects.get(pk=pk)
	serializer = ProductSerializer(product, many=False)

	return Response(serializer.data)

@api_view(['POST'])
def productCreate(request):
	serializer = TaskSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
	product = Product.objects.get(pk=pk)
	serializer = TaskSerializer(instance=product, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE'])
def productDelete(request, pk):
	product = Product.objects.get(pk=pk)
	product.delete()

	return Response('Product successfully deleted!')
