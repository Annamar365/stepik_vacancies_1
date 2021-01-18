"""stepik_vacancies URL Configuration

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

from vacancies.views import company_view
from vacancies.views import custom_handler404
from vacancies.views import custom_handler500
from vacancies.views import main_view
from vacancies.views import vacancies_cat_view
from vacancies.views import vacancies_view
from vacancies.views import vacancy_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main'),
    path('vacancies/', vacancies_view, name='vacancies'),
    path('vacancies/cat/<str:cat>/', vacancies_cat_view, name='vacancies_cat'),
    path('companies/<int:company_id>/', company_view, name='companies'),
    path('vacancies/<int:vacancy_id>/', vacancy_view, name='vacancy'),
]

handler404 = custom_handler404
handler500 = custom_handler500
