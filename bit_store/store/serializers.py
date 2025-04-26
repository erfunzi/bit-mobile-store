from rest_framework import serializers
from .models import Category, Product
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid username or password.")

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

    def validate_name (self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Category name must be at least 3 characters long.")
        if Category.objects.filter(name=value).exists() and self.instance is None:
            raise serializers.ValidationError("Category with this name already exists.")
        return value

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'category_id', 'price', 'stock', 'description', 'created_at', 'created_by']
        read_only_fields = ['created_by'] 
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock cannot be negative.")
        return value
    
    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Product name must be at least 5 characters long.")
        if value.isalnum() == False:
            raise serializers.ValidationError("Product name must be alphanumeric.")
        return value
    
    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Description must be at least 10 characters long.")
        if len(value) > 200:
            raise serializers.ValidationError("Description must be at most 200 characters long.")
        return value

    def validate(self, data):
        price = data.get('price')
        stock = data.get('stock')
        if price > 10000 and stock < 5 :
            raise serializers.ValidationError("If the price is greater than 10000, stock must be at least 5.")
        return data
    

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        if len(data['password']) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in data['password']):
            raise serializers.ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in data['password']):
            raise serializers.ValidationError("Password must contain at least one letter.")
        if not any(char in '!@#$%^&*()_+' for char in data['password']):
            raise serializers.ValidationError("Password must contain at least one special character.")
        if data['password'] == data['username']:
            raise serializers.ValidationError("Password cannot be the same as username.")
        if data['password'] == data['email']:
            raise serializers.ValidationError("Password cannot be the same as email.")
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    