import re

from django.conf import settings

from rest_framework import serializers

from app.models import Category, Shop, Product, ProductInfo, User, Contact, ProductParameter, OrderItem, Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('id', 'name', 'url', 'state',)
        read_only_fields = ('id',)


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
        read_only_fields = ('id',)
        extra_kwargs = {
            'user': {'write_only': True}
        }

    # проверим формат телефона
    def validate_phone(self, value):
        if not re.match(r'^\+\d{1,11}\(\d{3}\)\d{7}', value):
            raise serializers.ValidationError("Неверный формат номера телефона, формат "
                                              "+<код страны>(<код оператора>)<номер> +7(123)1234567")

        return value


class ContactSerializerCreate(ContactSerializer):
    # проверим количество контактов, должно быть не больше LIMIT_CONTACTS (указываетс в settings)
    def validate(self, attrs):

        list_contact = Contact.objects.filter(user=self.initial_data['user'])

        if len(list_contact) >= settings.LIMIT_CONTACTS:
            raise serializers.ValidationError(f"Превышен лимит контактов, не может быть больше "
                                              f"{settings.LIMIT_CONTACTS}")
        return attrs


class UserSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'company', 'position', 'contacts')
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ProductParameterSerializer(serializers.ModelSerializer):
    parameter = serializers.StringRelatedField()

    class Meta:
        model = ProductParameter
        fields = ('parameter', 'value',)


class ProductInfoSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_parameters = ProductParameterSerializer(read_only=True, many=True)

    class Meta:
        model = ProductInfo
        fields = ('id', 'model', 'product', 'shop', 'quantity', 'price', 'price_rrc', 'product_parameters',)
        read_only_fields = ('id',)


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ('id', 'product_info', 'quantity', 'order',)
        read_only_fields = ('id',)
        extra_kwargs = {
            'order': {'write_only': True}
        }


class OrderSerializer(serializers.ModelSerializer):
    ordered_items = OrderItemSerializer(read_only=True, many=True)

    class Meta:
        model = Order
        fields = ('id', 'ordered_items', 'state', 'dt', )
        read_only_fields = ('id',)

