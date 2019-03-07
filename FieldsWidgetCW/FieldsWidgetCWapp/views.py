from django.http import HttpResponse
from django.shortcuts import render
from .forms import heroForm


# Create your views here.

# RENDERS INDEX PAGE FROM URL
def index(request):
    return render(request, 'FieldsWidgetCWapp/index.html')


# RENDERS FORM BY INJECTION
def form(request):
    return render(request, 'FieldsWidgetCWapp/form.html', {'form': heroForm()})


# SAVES FORM FROM POST
def thankyou(request):
    new_form = heroForm(request.POST or None)
    if new_form.is_valid():
        new_form.save()

    return render(request, 'FieldsWidgetCWapp/thankyou.html', {'form': new_form})
