from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jsonfield

# define model for restaurant data
class Restaurant(models.Model):
    restaurantId = models.AutoField(primary_key=True, null=False, db_column='restaurantId')
    restaurantName = models.CharField(max_length=200, null=False, db_column='restaurantName')
    restaurantLocation = models.CharField(max_length=200, null=True, db_column='restaurantLocation')
    restaurantContact = models.CharField(max_length=50, null=True, db_column='restaurantContact')
    restaurantOpenTime = models.TimeField(blank=False, db_column='restaurantOpenTime')
    restaurantCloseTime = models.TimeField(blank=False, db_column='restaurantCloseTime')
    restaurantSales = jsonfield.JSONField(max_length=1000, null=True, db_column='restaurantSales')
    restaurantLongtitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    restaurantLatitude = models.DecimalField(max_digits=15, decimal_places=10, null=True)
    restaurantImage = models.CharField(max_length=200, null=True, db_column='restaurantImage')

    def __unicode__(self):
        return self.restaurantName

    class Meta:
        db_table = 'restaurant'

# define model for employee data
class Employee(models.Model):
    employeeId = models.AutoField(primary_key=True, null=False, db_column='employeeId')
    employeeBelong = models.ForeignKey(Restaurant, related_name='employee', db_column='employeeBelong',
                                       on_delete=models.CASCADE)
    employeeJobnumber = models.CharField(max_length=100, null=False, db_column='employeeJobnumber')
    employeeTitle = models.CharField(max_length=100, db_column='employeeTitle')
    employeeSex = models.IntegerField(null=False, db_column='employeeSex')
    employeeFirstname = models.CharField(max_length=100, null=True, db_column='employeeFirstname')
    employeeLastname = models.CharField(max_length=100, null=True, db_column='employeeLastname')
    employeeContact = models.CharField(max_length=100, null=True, db_column='employeeContact')
    employeeSalary = models.DecimalField(max_digits=8, decimal_places=2, max_length=10, null=False,
                                         db_column='employeeSalary')
    employeePhoto = models.CharField(max_length=200, db_column='employeePhoto')

    def __unicode__(self):
        return self.employeeFirstname + " " + self.employeeLastname

    class Meta:
        db_table = 'employee'

# define model for recipe data
class Recipe(models.Model):
    recipeId = models.AutoField(primary_key=True, null=False, db_column='recipeId')
    recipeName = models.CharField(max_length=100, null=False, db_column='recipeName')
    recipePrice = models.DecimalField(max_digits=8, decimal_places=2, max_length=10, null=False,
                                      db_column='recipePrice')
    recipeDescription = models.TextField(null=True, db_column='recipeDescription')
    recipeImagepath = models.CharField(max_length=200, db_column='recipeImagepath')

    def __unicode__(self):
        return self.recipeName

    class Meta:
        db_table = 'recipe'
