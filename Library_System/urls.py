"""Library_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from library_app.views import user_login, register, index, student_home, librarian_home, user_logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('', index, name='home'),
    path('s_home/', student_home, name='s_home'),
    path('l_home/', librarian_home, name='l_home'),
    path('logout/', user_logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
