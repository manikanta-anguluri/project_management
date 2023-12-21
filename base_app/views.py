from django.shortcuts import render
from django.contrib.auth.models import User
from project_management_app.models import Project,Task
from register_app.models import Company

# Create your views here.

def renderHome(request):
    return render(request,"base_home.html")

def renderIndex(request):
    return render(request,"index.html")


def dashboard(request):
    if request.user.is_superuser:
        users = User.objects.all()
        companies = Company.objects.all()
        projects = Project.objects.all()
        tasks=Task.objects.all()
    else:
        users = User.objects.all()
        companies = Company.objects.all()
        # users = User.objects.filter(assign=request.user)
        # companies = Company.objects.filter(assign=request.user)
        projects = Project.objects.filter(assign=request.user)
        tasks=Task.objects.filter(assign=request.user) 
    context = {
        'users' : users,
        'companies' : companies,
        'projects' : projects,
        'tasks' : tasks,
    }
    return render(request, 'dashboard.html', context)    