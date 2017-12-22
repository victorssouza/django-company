from django.contrib import admin
from django.urls import path, re_path
# Custom views
from employees import views

urlpatterns = [
    path('django-admin/', admin.site.urls),
    re_path(r'^$', views.home),
    re_path(r'^api/v1/employee/$', views.rest_all_employees, name='all_employees'),
    re_path(r'^api/v1/employee/(?P<employee_id>[0-9]+)/$', views.rest_specific_employee, name='specific_employee'),
]
