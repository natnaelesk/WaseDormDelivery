

# urls.py
from django.urls import path , include
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.HomeView , name='home'), 
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path("logout", LogoutView.as_view(next_page='login'), name='logout'),
     path('profile/', views.user_profile, name='user_profile'),

     path('edit_profile/', views.EditUserProfileView.as_view(), name='edit_profile'),
     
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
