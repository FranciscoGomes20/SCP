from django.contrib import admin
from pkg_resources import Requirement
from .models import *

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Status)
admin.site.register(Setor)
admin.site.register(Chamado)
