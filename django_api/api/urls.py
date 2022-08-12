from django.urls import path

from . import views

urlpatterns = [
    path('', views.view_employee),
    path('add-employee', views.add_employee),
    path('update-employe', views.update_employee),
    path('delete- employee', views.delete_empoyee),




]

