from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Employee
# Functions for HTTP-Methods
from .data_manager.database_crud_manager import create_new_employee, update_employee_attributes, delete_employee
from .data_manager.beautify_utils import parse_employee_data

def home(request):
    return render(request, 'employees/home.html')

# Decorator needed due to Cross Site Request Forgeries
@csrf_exempt
def rest_all_employees(request):
    if request.method == 'GET':
        response_data = []
        employees = Employee.objects.order_by('employee_created_date')
        for employee in employees:
            temp_parsed_data = parse_employee_data(employee.employee_name, employee.employee_email, employee.employee_department)
            response_data.append(temp_parsed_data)
        # safe is set to False due to a object return instead of an iterable
        return JsonResponse(response_data, safe=False)
    elif request.method == 'POST':
        operation_status, operation_message = create_new_employee(request.body)
        if operation_status:
            return JsonResponse({'message': str(operation_message)}, status=201)
        else:
            return JsonResponse({'message': str(operation_message)}, status=500)
    else:
        return JsonResponse({'message':'method not allowed'}, status=503)

# Decorator needed due to Cross Site Request Forgeries
@csrf_exempt
def rest_specific_employee(request, employee_id=None):
    if request.method == 'GET':
        employee = get_object_or_404(Employee, id=employee_id)
        response_data = parse_employee_data(employee.employee_name, employee.employee_email, employee.employee_department)
        return JsonResponse(response_data)
    elif request.method == 'PUT':
        operation_status, operation_message = update_employee_attributes(employee_id, request.body)
        if operation_status:
            return JsonResponse({'message': str(operation_message)}, status=201)
        else:
            return JsonResponse({'message': str(operation_message)}, status=500)
    elif request.method == 'DELETE':
        operation_status, operation_message = delete_employee(employee_id)
        if operation_status:
            return JsonResponse({'message': str(operation_message)}, status=202)
        else:
            return JsonResponse({'message': str(operation_message)}, status=500)
    else:
        return JsonResponse({'message':'method not allowed'}, status=503)
