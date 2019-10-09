from django.urls import path
from .views import *

urlpatterns = [
    path('livro_list/', livro_list, name='listar_livros'),
    path('livro_new/', livro_new, name='livro_new'),
    path('livro_edit/(?P<pk>[0-9]+)', livro_edit, name='livro_edit'),
    path('livro_remove/(?P<pk>[0-9]+)', livro_remove, name='livro_remove')
]
