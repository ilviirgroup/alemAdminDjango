from rest_framework import serializers
from .models import Brand, Products, Category, Color, Gender, Size, Status, Subcategory, Update, Messages, UserAlem
from .models import Orders, Favorites


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Brand
        fields = ('url', 'name', 'products', )


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Products
        fields = ('name', 'description', 'photo', 'brand', 'category', 'color', 'gender', 'size', 'status',
                  'subcategory', 'update',)



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Category
        fields = ('url', 'pk', 'ai', 'name', 'products', 'photo')

class ColorSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Color
        fields = ('url', 'name', 'products', )

class GenderSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Gender
        fields = ('url', 'name', 'products', )

class SizeSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Size
        fields = ('url', 'name', 'subcategory','products', )

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Status
        fields = ('url', 'name', 'products', )

class SubcategorySerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Subcategory
        fields = ('url', 'name', 'category', 'products', )

class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail')

    class Meta:
        model = Update
        fields = ('url', 'update', 'products')

class MessageSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=UserAlem.objects.all(), slug_field='username')
    #user = serializers.HyperlinkedRelatedField(
        #many=True,
        #read_only=True,
        #view_name='messages-detail')

    class Meta:
        model = Messages
        fields = ('url', 'user', 'text', 'date')

class OrdersSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=UserAlem.objects.all(), slug_field='username')

    class Meta:
        model = Orders
        fields = ('url', 'user', 'ai', 'color', 'completed', 'date', 'name', 'quantity', 'size')

class FavoritesSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(queryset=UserAlem.objects.all(), slug_field='username')

    class Meta:
        model = Favorites
        fields = ('url', 'user', 'ai', 'color', 'date', 'name', 'size')

class UserAlemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserAlem
        fields = ('url', 'username', 'phone', 'email')