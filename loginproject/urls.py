from django.contrib import admin
from django.urls import path,include
import loginapp.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginapp.views.home, name='home'),
    path('login/',loginapp.views.login, name='login'),
    path('signup/',loginapp.views.signup, name='signup'),
    path('logout/',loginapp.views.logout, name='logout'),
    path('accounts/',include('allauth.urls')),
]
