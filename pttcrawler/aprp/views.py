import json

from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from aprp.serializers import CategorySerializer, MarketSerializer, ProductSerializer, DailyTranSerializer
from aprp.models import Category, Market, Product, DailyTran


class CategoryList(APIView):

    def get(self, request, format=None):

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    permission_classes = (IsAuthenticated,)


class MarketList(APIView):

    def get(self, request, format=None):

        market = Market.objects.all()
        serializer = MarketSerializer(market, many=True)
        return Response(serializer.data)
    permission_classes = (IsAuthenticated,)


class ProductList(APIView):

    def get(self, request, format=None):

        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)
    permission_classes = (IsAuthenticated,)


class DailyTranList(APIView):

    def get(self, request, format=None):

        dailytran = DailyTran.objects.all()
        serializer = DailyTranSerializer(dailytran, many=True)
        return Response(serializer.data)
    permission_classes = (IsAuthenticated,)
