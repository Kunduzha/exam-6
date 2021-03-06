"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import main_page, dell_comment, update_comment, add_comment

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', main_page, name='all_page'),
    # path('<int:pk>/update', update_comment, name='update_comment'),
    # path('<int:pk>/delete', dell_comment, name='delete_comment'),
    # path('<int:pk>/delete', add_comment, name='add_comment'),

]
