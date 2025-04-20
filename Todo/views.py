from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(requests):
    return HttpResponse("Hello, world. You're you doing my people")

def task_list(request):
    tasks = Task.objects.all().order_by('-date_created')
    return render(request, 'task_list.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')


#def contact_page(request):
    #return render(request, 'contact/contact.html')