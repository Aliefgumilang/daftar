from django.shortcuts import render, redirect
from pengunjung.models import *

def list_pengunjung(request):
    tempalte_name = 'list_pengunjung.html'
    pengunjung_list = Daftar.objects.all()
    context = {
        'title' : 'ini adalah halaman pengunjung',
        'pengunjung' :pengunjung_list
    }
    return render(request, tempalte_name, context)

def add_pengunjung(request):
    tempalte_name = 'add_pengunjung.html'
    kategori = Kategori.objects.all()
    
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskrpisi')

        # panggil kategori dulu
        get_kategori = Kategori.objects.get(nama=input_kategori)

        # simpan produk dengan relasi tabel kategori
        Daftar.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            kategori = get_kategori,
        )
        return redirect(list_pengunjung)

    context = {
        'title' : 'ini adalah halaman tambah barang',
        'kategori' :kategori
    }
    return render(request, tempalte_name, context)

def update_pengunjung(request, id):
    tempalte_name = 'add_pengunjung.html'
    kategori = Kategori.objects.all()
    get_daftar = Daftar.objects.get(id=id)
    
    if request.method == "POST":
        input_kategori = request.POST.get('kategori')
        input_nama = request.POST.get('nama')
        input_deskripsi = request.POST.get('deskrpisi')

        # panggil kategori dulu
        get_kategori = Kategori.objects.get(nama=input_kategori)

        # simpan produk dengan relasi tabel kategori
        get_daftar.nama = input_nama
        get_daftar.deskripsi = input_deskripsi
        get_daftar.kategori = get_kategori
        get_daftar.save()
        return redirect(list_pengunjung)

    context = {
        'title' : 'ini adalah halaman tambah barang',
        'kategori' :kategori,
        'get_daftar' :get_daftar,

    }
    return render(request, tempalte_name, context)


def delete_pengunjung(request, id):
    pengunjung = Daftar.objects.get(id=id).delete()
    return redirect(list_pengunjung)