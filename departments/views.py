from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Department

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, 'departments/department_list.html', {
        'departments': departments
    })

@login_required
def add_department(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')

        Department.objects.create(
            name=name,
            description=description
        )
        return redirect('department_list')

    return render(request, 'departments/add_department.html')


# Create your views here.
