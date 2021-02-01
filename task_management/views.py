from django.shortcuts import render
from .models import Task

def index(request):
    data=Task.objects.all().order_by("-Date")[:3]
    print(data)
    
    context={'fields':data}
    return render(request, 'task_management/index.html',context)
