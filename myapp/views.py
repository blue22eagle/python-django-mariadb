from django.shortcuts import render, redirect, HttpResponse
from .forms import myTableForm
from .models import myTable
import datetime

# Create your views here.
def hello(request):
    mytest= datetime.datetime.now().date()
    mytest2= 123
    today= datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, 'hello.html', {'today': today, 'daysOfWeek': daysOfWeek})

def show(request):
    items= myTable.objects.all()
    return render(request, 'show.html', {'items': items})

def add(request):
    if request.method== 'POST':
        form= myTableForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form= myTableForm()
    return render(request, 'add.html', {'form': form})

def update(request, id):
    item= myTable.objects.get(id= id)
    form= myTableForm(instance= item)
    if request.method== 'POST':
        postForm= myTableForm(request.POST, instance= item)
        if postForm.is_valid():
            postForm.save()
            print(request, 'Data has been updated.')
            return redirect('/show')
    return render(request, 'update.html', {'form': form, 'item': item})

def delete(request, id):
    item= myTable.objects.get(id= id)
    item.delete()
    return redirect('/show')