from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=250)
    employee_email = models.CharField(max_length=100)
    employee_department = models.CharField(max_length=100)
    employee_created_date = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_name

    def employee_created_date_pretty(self):
        return self.employee_created_date.strftime('%b %e %Y')