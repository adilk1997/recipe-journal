from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('recipes/', views.RecipeList.as_view(), name='recipe-index'),
    path('recipes/create/', views.RecipeCreate.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/', views.RecipeDetail.as_view(), name='recipe-detail'),
    path('recipes/<int:pk>/update/', views.RecipeUpdate.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe-delete'),
    path('categories/', views.CategoryList.as_view(), name='category-index'),
    path('categories/create/', views.CategoryCreate.as_view(), name='category-create'),
    path('categories/<int:pk>/update/', views.CategoryUpdate.as_view(), name='category-update'),
    path('categories/<int:pk>/delete/', views.CategoryDelete.as_view(), name='category-delete'),
    ]