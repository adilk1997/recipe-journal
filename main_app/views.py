from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe
from .models import Category


class Home(LoginView):
    template_name = "home.html"


def about(request):
    return render(request, "about.html")


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form, 'error_message': error_message})

class RecipeList(LoginRequiredMixin, ListView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


class RecipeDetail(LoginRequiredMixin, DetailView):
    model = Recipe

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


class RecipeCreate(LoginRequiredMixin, CreateView):
    model = Recipe
    fields = ["title", "prep_time", "cook_time", "ingredients", "instructions", "category"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeUpdate(LoginRequiredMixin, UpdateView):
    model = Recipe
    fields = ["title", "prep_time", "cook_time", "ingredients", "instructions", "category"]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)


class RecipeDelete(LoginRequiredMixin, DeleteView):
    model = Recipe
    success_url = reverse_lazy("recipe-index")

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)
    
class CategoryList(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ["name"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ["name"]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("category-index")

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)