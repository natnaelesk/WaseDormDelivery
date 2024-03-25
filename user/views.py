
#views.py
from django.contrib.auth import get_user_model
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserCreationForm 
from .forms import UserProfileForm
from .models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from django.db.models import Sum
from django.db.models import Q  
from Menu.models import MenuItem , Restaurant


def HomeView(request):
     # Assuming there's only one restaurant in the database
    restaurant = Restaurant.objects.first()
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    # Search functionality
    search_query = request.GET.get('search_query')
    if search_query:
        menu_items = menu_items.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))

    return render(request, 'Menu/menu_item_list.html', {'restaurant': restaurant, 'menu_items': menu_items})

    
class SignUp(View):
    template_name = 'user/signup.html'

    def get(self, request, *args, **kwargs):
        form = UserProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Menu:menu_item_list')  # Redirect to the home page after successful signup
        return render(request, self.template_name, {'form': form})

class LoginView(View):
    template_name = 'user/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('Menu:menu_item_list')  # Redirect to the home page after successful login
            else:
                # Display an error message if login fails
                messages.error(request, 'Invalid username or password.')

        return render(request, self.template_name, {'form': form})

@login_required
def user_profile(request):
    profile = request.user  # Use the/profile/ user instance directly
    return render(request, 'user/user_profile.html', {'profile': profile})






@method_decorator(login_required, name='dispatch')
class EditUserProfileView(View):
    template_name = 'user/edit_user_profile.html'

    def get(self, request, *args, **kwargs):
        profile = request.user
        form = UserProfileForm(instance=profile)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        profile = request.user
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            login(request, request.user)
            return redirect('Menu:menu_item_list')
        else:
            messages.error(request, 'Failed to update profile. Please check the provided information.')
            return render(request, self.template_name, {'form': form})