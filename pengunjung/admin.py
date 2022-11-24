from django.contrib import admin
from pengunjung.models import *
# Register your models here.

admin.site.register(Kategori)

class DaftarAdmin(admin.ModelAdmin):
    list_display = ['nama','deskripsi',]
admin.site.register(Daftar, DaftarAdmin)