
from django.shortcuts import render

def principal(request):

    return render(request, 'principal.html')

def segunda(request):

    return render(request, 'segundo.html')