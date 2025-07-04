
from decimal import Decimal
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
    
    total = serializers.SerializerMethodField() 

    class Meta:
        model = ExpenseIncome
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at'] 

    
    def get_total(self, obj):
        
        return obj.total


    def calculate_total(self, amount, tax, tax_type):
        amount_decimal = Decimal(str(amount))
        if tax is None:
            tax_decimal = Decimal(0)
        else:
            tax_decimal = Decimal(str(tax))

        if tax_type == 'percentage':
            return amount_decimal * (1 + tax_decimal / 100)
        elif tax_type == 'flat':
            return amount_decimal + tax_decimal
        else:
            return amount_decimal

    def create(self, validated_data):
        
        return super().create(validated_data)

    def update(self, instance, validated_data):
       

        
        updated_instance = super().update(instance, validated_data) 

        

        return updated_instance
    

