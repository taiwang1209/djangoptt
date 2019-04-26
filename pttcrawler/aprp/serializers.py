from rest_framework import serializers

from aprp.models import Category, Market, Product, DailyTran


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DailyTranSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyTran
        fields = '__all__'
