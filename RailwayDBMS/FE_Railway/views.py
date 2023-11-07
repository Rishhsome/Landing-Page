from django.shortcuts import render
from .models import RailwaySystem, Railway, Train
from .forms import RailwaySystemForm, RailwayForm, TrainForm


def index(request):
    return render(request, 'index.html')


def submit_railway_system(request):
    if request.method == 'POST':
        form = RailwaySystemForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form, 'success_message': 'Details added successfully.'})
        else:
            return render(request, 'index.html', {'form': form, 'error_message': 'Failed to add details. Please check the form.'})
    else:
        form = RailwaySystemForm()

    return render(request, 'index.html', {'form': form})



def submit_railway(request):
    if request.method == 'POST':
        form = RailwayForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form, 'success_message': 'Details added successfully.'})
        else:
            return render(request, 'index.html', {'form': form, 'error_message': 'Failed to add details. Please check the form.'})
    else:
        form = RailwayForm()

    return render(request, 'index.html', {'form': form})

def submit_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {'form': form, 'success_message': 'Details added successfully.'})
        else:
            return render(request, 'index.html', {'form': form, 'error_message': 'Failed to add details. Please check the form.'})
    else:
        form = TrainForm()

    return render(request, 'index.html', {'form': form})