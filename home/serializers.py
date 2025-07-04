# home/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

from home.models import ExpenseIncome

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    email = serializers.EmailField(required=True) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

    def validate_email(self, value):
        
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return value
    

class ExpenseIncomeSerializer(serializers.ModelSerializer):
        
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True) 

    class Meta:
        model = ExpenseIncome
            
        fields = '__all__'
            
        read_only_fields = ['user', 'created_at', 'updated_at'] 
