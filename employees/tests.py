from django.test import TestCase
from .models import Employee
from .data_manager.database_crud_manager import create_new_employee, update_employee_attributes, delete_employee
from .data_manager.beautify_utils import parse_employee_data

class EmployeeTestCase(TestCase):
    def setUp(self):
        Employee.objects.create(employee_name="Arnaldo Pereira", employee_email="arnaldo@luizalabs.com", employee_department="Architecture")
        Employee.objects.create(employee_name="Renato Pedigoni", employee_email="renato@luizalabs.com", employee_department="E-commerce")
        Employee.objects.create(employee_name="Thiago Catoto", employee_email="catoto@luizalabs.com", employee_department="Mobile")

    def test_parser(self):
        parsed_response = parse_employee_data("Arnaldo Pereira", "arnaldo@luizalabs.com", "Architecture")
        self.assertEqual(parsed_response['name'], 'Arnaldo Pereira')
        self.assertEqual(parsed_response['email'], 'arnaldo@luizalabs.com')
        self.assertEqual(parsed_response['department'], 'Architecture')

    def test_create_employee(self):
        """ Validating scenarios when creating a new employee """
        correct_payload = '{ "name": "New Employee", "email": "newguy@luizalabs.com", "department": "Developer" }'
        create_new_employee(correct_payload)
        self.assertEqual(Employee.objects.get(employee_email='newguy@luizalabs.com').employee_name, 'New Employee')
        
        missing_attribute_payload = '{ "name": "Missing Dep Employee", "email": "missingdep@luizalabs.com" }'
        status, message = create_new_employee(missing_attribute_payload)
        self.assertFalse(status)

        malformed_payload = { "name": "New Malformed Employee", "email": "newmalformedguy@luizalabs.com", "department": "Developer" }
        self.assertRaises(TypeError, lambda: create_new_employee(malformed_payload))

    def test_delete_employee(self):
        """ Validating scenarios when deleting an existent employee """
        operation_status, operation_message = delete_employee(2)
        self.assertTrue(operation_status)

        operation_status, operation_message = delete_employee(99)
        self.assertFalse(operation_status)

        operation_status, operation_message = delete_employee('some_id')
        self.assertFalse(operation_status)
    
    def test_update_employee_attributes(self):
        """ Validating scenarios when updating an existent employee """
        correct_payload = '{ "name": "Catoto New Name", "department": "PMO" }'
        update_employee_attributes(3, correct_payload)
        self.assertEqual(Employee.objects.get(employee_email='catoto@luizalabs.com').employee_name, 'Catoto New Name')
        self.assertEqual(Employee.objects.get(employee_email='catoto@luizalabs.com').employee_department, 'PMO')

        malformed_payload = { "name": "Catoto New Name", "department": "PMO" }
        self.assertRaises(TypeError, lambda: update_employee_attributes(1, malformed_payload))

        operation_status, operation_message = update_employee_attributes('some_id', correct_payload)
        self.assertFalse(operation_status)


