# home/views.py
from rest_framework import generics, status, viewsets,permissions
from rest_framework.response import Response
from django.contrib.auth.models import User

from home.models import ExpenseIncome 
from .serializers import ExpenseIncomeSerializer, UserRegistrationSerializer 

class UserRegistrationView(generics.CreateAPIView):
    # API endpoint that will allows a new user to be registered.
    # Requires Username, email, passwords
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [] 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "message": "User registered successfully",
            "username": user.username,
            "email": user.email
        }, status=status.HTTP_201_CREATED)
    

class ExpenseIncomeViewSet(viewsets.ModelViewSet):
    # API endpoint that allows expense/income records to be viewed and edited.
    # Requires JWT authentication for all operations
    serializer_class = ExpenseIncomeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        
        if self.request.user.is_superuser:
            return ExpenseIncome.objects.all()
        
        return ExpenseIncome.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        
        serializer.save(user=self.request.user)