from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='departments')

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')

class Product(models.Model):
    name = models.CharField(max_length=100)

class Description(models.Model):
    name = models.CharField(max_length=100)
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='descriptions')

class Student(models.Model):
    name = models.CharField(max_length=100)

class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='courses')


employees = Employee.objects.prefetch_related('department')