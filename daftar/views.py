from multiprocessing import context
from django.shortcuts import render

def index(request):
    tempalte_name = 'index.html'
    context = {
        'title' : 'Selamat datang di halaman home'
    }
    return render(request, tempalte_name, context)

def about(request):
    tempalte_name = 'about.html'
    context = {
        'title' : 'Selamat datang di halaman about'
    }
    return render(request, tempalte_name, context)