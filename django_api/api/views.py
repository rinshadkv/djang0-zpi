from urllib import request
from django.shortcuts import render
from django.http.response import JsonResponse
from api.models import Employee
from api.serializers import ApiSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
# from rest_framework import permissions
# Create your views here.


@csrf_exempt
@api_view(["GET"])
def view_employee(request):
   
    if request.method=="GET":
        employee=Employee.objects.all()
        employee_serlizer=ApiSerializer(employee,many='True')
    
        return JsonResponse(employee_serlizer.data,safe=False)


@api_view(["POST"])
def add_employee(request):
   if request.method=="POST":
        employeedata = JSONParser().parse(request)
        serializer = ApiSerializer(data=employeedata)
        if serializer.is_valid():
            serializer.save()

        return JsonResponse('Data inserted Successfully..!',safe=False)




@api_view(["PUT"])
def update_employee(request):
    if request.method=="PUT":
        employeedata = JSONParser().parse(request)
        employee = Employee.objects.get(id=employeedata['id'])
        employee_serializer = ApiSerializer(employee,employeedata)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse('Data updated Successfully..!',safe=False)
    return JsonResponse('Failed to update..!',safe=False)

@api_view(["DELETE"])
def delete_empoyee(request):
    if request.method=='DELETE':
        employee = Employee.objects.get(id=id)
        employee.delete()
        return JsonResponse('Data deleted Successfully..!',safe=False)



