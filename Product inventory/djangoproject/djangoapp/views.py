
from django.shortcuts import render, redirect
from .models import Computer, Operating_system
from .forms import ComputerSearchForm, ComputerForm
from django.http import HttpResponse
import csv
from django.contrib import messages



def home(request):
    title = 'Computer Inventory'
    context = {'title':title}
    return render(request, 'task/home.html', context)


def computer_list(request):
    title = 'Computer List'
    quearyset = Computer.objects.all()
    form = ComputerSearchForm(request.POST)
    context = {
        'title':title, 
        'quearyset':quearyset,
        'form':form
            }
    if request.method == 'POST':
        queryset = Computer.objects.all().order_by('-timestamp').filter(user_name__icontains=form['user_name'].value())
        context = {
        'title': title,
        'queryset': queryset,
        'form': form,
        }
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="Computer list.csv"'
            writer = csv.writer(response)
            writer.writerow(['COMPUTER NAME', 'IP Address', 'MAC ADDRESS', 'OS', 'USERNAME', 'LOCATION', 'PURCHASE DATE', 'TIMESTAMP'])
            instance = queryset
            for row in instance:
                writer.writerow([row.computer_name, row.IP_address, row.MAC_address, row.operating_system, row.user_name, row.location, row.purchase_date, row.timestamp])
            return response
    return render(request, 'task/computer_list.html', context)


def computer_entry(request):
    title = 'Add Computer'
    form = ComputerForm()
    if request.method == 'POST':
        form = ComputerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
        return redirect('/computer_list/')
    context = {'title':title, 'form':form}
    return render(request, 'task/computer_entry.html', context)


def computer_edit(request, pk):
    instance = Computer.objects.get(id=pk)
    form = ComputerForm(instance = instance)
    if request.method == 'POST':
        form = ComputerForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('computer_list')
    context = {
        "title": 'Edit' + str(instance.computer_name),
        "instance": instance,
        "form": form
    }
    return render(request, 'task/computer_entry.html', context)



def delete(request, pk):
    item = Computer.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('computer_list')
    context = {'item':item}
    return render(request, 'task/delete.html', context)
