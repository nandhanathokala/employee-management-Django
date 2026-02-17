from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee
from departments.models import Department

@login_required
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees/employee_list.html', {
        'employees': employees
    })

@login_required
def add_employee(request):
    departments = Department.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        department_id = request.POST.get('department')

        Employee.objects.create(
            name=name,
            email=email,
            phone=phone,
            department_id=department_id
        )
        return redirect('employee_list')

    return render(request, 'employees/add_employee.html', {
        'departments': departments
    })

@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    departments = Department.objects.all()

    if request.method == "POST":
        employee.name = request.POST.get('name')
        employee.email = request.POST.get('email')
        employee.phone = request.POST.get('phone')
        employee.department_id = request.POST.get('department')
        employee.save()

        return redirect('employee_list')

    return render(request, 'employees/edit_employee.html', {
        'employee': employee,
        'departments': departments
    })

@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')


# Create your views here.
