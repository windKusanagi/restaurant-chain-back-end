from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Restaurant, Employee, Recipe
from .serializers import RestaurantSerializer, EmploySeralizer, RecipeSerializer


# Create your views here.


# An API-based view for retrieve restaurant list and create new restaurant
class getPostRestaurantsView(APIView):
    """
    Get all restaurants,Create Restaurant, currently no pagination
    """

    def get(self, request):
        restaurants = Restaurant.objects.all()
        # Call ModelSerializer to automatically make the response body
        restaurantSer = RestaurantSerializer(restaurants, many=True)
        return Response(restaurantSer.data)

    def post(self, request):
        data = request.data['data']
        restaurantSer = RestaurantSerializer(data=data)
        # Call ModelSerializer to automatically check the post data and make the response body
        if restaurantSer.is_valid():
            restaurantSer.save()
            return Response(restaurantSer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(restaurantSer.errors, status=status.HTTP_400_BAD_REQUEST)


# An API-based view to get, update and delete restaurant data by primary key(id)
class getByIdDeleteUpdateRestaurantsView(APIView):
    """
    Get restaurant by id, Delete restaurant by id,update restaurant by id
    """

    def get(self, request, pk):
        restaurants = Restaurant.objects.get(restaurantId=pk)
        # Call ModelSerializer to automatically make the response body
        restaurantSerializer = RestaurantSerializer(restaurants)
        return Response(restaurantSerializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        data = request.data['data']
        origin = Restaurant.objects.get(restaurantId=pk)
        # Call ModelSerializer to automatically check the put data and make the response body
        restaurantSer = RestaurantSerializer(origin, data=data, partial=True)
        if restaurantSer.is_valid():
            restaurantSer.save()
        return Response(restaurantSer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        restaurant = Restaurant.objects.get(restaurantId=pk)
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# An API-based view to retrieve employee data
class getPostEmployee(APIView):
    """
    Get all employees,Create employee, currently no pagination
    """

    def get(self, request):
        employees = Employee.objects.all()
        employeeSer = EmploySeralizer(employees, many=True)
        # Call ModelSerializer to automatically make the response body
        return Response(employeeSer.data)

    def post(self, request):
        data = request.data['data']
        employeeSer = EmploySeralizer(data=data)
        # Call ModelSerializer to automatically check the post data and make the response body
        if employeeSer.is_valid():
            employeeSer.save()
            return Response(employeeSer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(employeeSer.errors, status=status.HTTP_400_BAD_REQUEST)

# An API-based view to get, update, delete an employee data by id
class getByIdDeleteUpdateEmployeeView(APIView):
    """
    Get employee by id, Delete employee by id,update employee by id
    """

    def get(self, request, pk):
        employee = Employee.objects.get(employeeId=pk)
        employeeSer = EmploySeralizer(employee)
        # Call ModelSerializer to automatically make the response body
        return Response(employeeSer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        data = request.data['data']
        employee = Employee.objects.get(employeeId=pk)
        employeeSer = EmploySeralizer(employee, data=data, partial=True)
        # Call ModelSerializer to automatically check the put data and make the response body
        if employeeSer.is_valid():
            employeeSer.save()
        return Response(employeeSer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        employee = Employee.objects.get(employeeId=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# An API-based view to retrieve recipes data
class getPostRecipeView(APIView):
    """
    Get all recipes,Create recipes, currently no pagination
    """

    def get(self, request):
        recipes = Recipe.objects.all()
        recipesSer = RecipeSerializer(recipes, many=True)
        # Call ModelSerializer to automatically make the response body
        return Response(recipesSer.data)

    def post(self, request):
        data = request.data['data']
        recipeSer = RecipeSerializer(data=data)
        # Call ModelSerializer to automatically check the post data and make the response body
        if recipeSer.is_valid():
            recipeSer.save()
            return Response(recipeSer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(recipeSer.data, status=status.HTTP_400_BAD_REQUEST)

# An API-based view to get, update, delete recipe data by id
class getByIdDeleteUpdateRecipe(APIView):
    """
    Get recipe by id, Delete recipe by id,update recipe by id
    """

    def get(self, request, pk):
        origin = Recipe.objects.get(recipeId=pk)
        recipeSer = RecipeSerializer(origin)
        # Call ModelSerializer to automatically make the response body
        return Response(recipeSer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        data = request.data['data']
        recipe = Recipe.objects.get(recipeId=pk)
        recipeSer = RecipeSerializer(recipe, data=data, partial=True)
        # Call ModelSerializer to automatically check the put data and make the response body
        if recipeSer.is_valid():
            recipeSer.save()
        return Response(recipeSer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        recipe = Recipe.objects.get(recipeId=pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

