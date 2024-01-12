from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import TodoForm
from .models import Task
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView,DeleteView


class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'details.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'task_p', 'date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')


# Create your views here.
def index(request):
    task1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Task(name=name, task_p=priority, date=date)
        task.save()
        return redirect('/')
    return render(request, 'index.html', {'task1': task1})


def delete(request, taskid):
    task = Task.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Task.objects.get(id=id)
    # new = TodoForm(request.POST or None, request.FILES, instance=task)
    # if new.is_valid():
    #     new.save()
    #     return redirect('/')
    return render(request, 'edit.html', {'task': task})
