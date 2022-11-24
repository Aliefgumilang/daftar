from django.urls import path
from pengunjung.views import *

urlpatterns = [
    path('list', list_pengunjung, name='list_pengunjung'),
    path('add', add_pengunjung, name='add_pengunjung'),
    path('update/<int:id>', update_pengunjung, name='update_pengunjung'),
    path('delete/<int:id>', delete_pengunjung, name='delete_pengunjung'),
]
