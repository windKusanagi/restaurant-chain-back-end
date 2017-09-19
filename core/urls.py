from django.conf.urls import url
from . import views


# Define URL and the corresponding Views
urlpatterns = [
    # -------------------

    url('^restaurants/$', view=views.getPostRestaurantsView.as_view(), name="resaurantCreate_GetList"),
    url('^restaurants/(?P<pk>\d+)/$', view=views.getByIdDeleteUpdateRestaurantsView.as_view(), name="restaurantGetById_Delete"),

    # -------------------

    url('^employees/$', view=views.getPostEmployee.as_view(), name='getCreateEmployee'),
    url('^employees/(?P<pk>\d+)/$', view=views.getByIdDeleteUpdateEmployeeView.as_view(), name='getByIdDeleteUpdateEmployee'),

    # -------------------

    url('^recipes/$', view=views.getPostRecipeView.as_view(), name='getCreateRecipes'),
    url('^recipes/(?P<pk>\d+)/$', view=views.getByIdDeleteUpdateRecipe.as_view(), name='getByIdDeleteUpdateRecipe'),

    # ---------------------
]
