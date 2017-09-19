from rest_framework import serializers
from .models import Restaurant, Employee, Recipe


# Define serializer for restaurant model
class RestaurantSerializer(serializers.ModelSerializer):
    # Need to specify jsonfile for serializer
    restaurantSales = serializers.JSONField()
    class Meta:
        model = Restaurant
        fields = ('restaurantId',
                    'restaurantName',
                    'restaurantLocation',
                    'restaurantContact',
                    'restaurantOpenTime',
                    'restaurantCloseTime',
                    'restaurantSales',
                    'restaurantLongtitude',
                    'restaurantLatitude',
                    'restaurantImage')

# Define serializer for recipe model
class EmploySeralizer(serializers.ModelSerializer):
    # need to specify foreign key for employee data
    employeeBelong = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())

    class Meta:
        model = Employee
        fields = ('employeeId','employeeBelong',
                    'employeeJobnumber','employeeTitle',
                    'employeeSex','employeeFirstname',
                    'employeeLastname','employeeContact',
                    'employeeSalary','employeePhoto')


# Define serializer for recipe model
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'
