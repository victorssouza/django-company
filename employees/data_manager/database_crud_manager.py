from ..models import Employee
import json

def create_new_employee(request_payload):
    # Validating payload format
    try:
        if request_payload == {} or request_payload == None or request_payload == '':
            return False, 'empty payload'
        request_payload = json.loads(request_payload)
    except ValueError as payload_error:  # includes simplejson.decoder.JSONDecodeError
        return False, 'got empty or malformed json payload'

    # Validating payload attributes
    if 'name' in request_payload:
        name = request_payload['name']
    else:
        return False, 'payload attribute expected: \'name\':'

    if 'email' in request_payload:
        email = request_payload['email']
    else:
        return False, 'payload attribute expected: \'email\':'

    if 'department' in request_payload:
        department = request_payload['department']
    else:
        return False, 'payload attribute expected: \'department\':'

    try:
        e = Employee.objects.create(employee_name=name, employee_email=email, employee_department=department)
    except Exception as e:
        return False, e
    return True, 'created employee \'{}\''.format(name)

def update_employee_attributes(id, request_payload):
    # Validating payload format
    try:
        if request_payload == {} or request_payload == None or request_payload == '':
            return False, 'empty payload'
        request_payload = json.loads(request_payload)
    except ValueError as payload_error:  # includes simplejson.decoder.JSONDecodeError
        return False, 'got empty or malformed json payload'
    
    try:
        e = Employee.objects.get(id=id)
    except Exception as e:
        return False, 'update failure: {}'.format(e)

    # Validating payload attributes
    if 'name' in request_payload:
        name = request_payload['name']
        e.employee_name = name
    else:
        name = None

    if 'email' in request_payload:
        email = request_payload['email']
        e.employee_email = email
    else:
        email = None

    if 'department' in request_payload:
        department = request_payload['department']
        e.employee_department = department
    else:
        department = None

    e.save()
    return True, 'updated employee \'{}\''.format(e.employee_name)

def delete_employee(id):
    try:
        e = Employee.objects.get(id=id)
        e.delete()
        e.save()
    except Exception as e:
        return False, 'delete failure: {}'.format(e)
    return True, 'deleted employee \'{}\''.format(e.employee_name)