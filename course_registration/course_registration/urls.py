from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users.views import register, user_login, dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('', include('users.urls')),
]