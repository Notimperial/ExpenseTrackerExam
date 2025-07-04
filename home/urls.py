
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseIncomeViewSet 

app_name = 'expenses'

router = DefaultRouter()
router.register(r'expenses', ExpenseIncomeViewSet, basename='expenses') 
urlpatterns = [
    path('', include(router.urls)), 
]