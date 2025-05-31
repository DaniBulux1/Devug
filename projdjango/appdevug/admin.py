from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Tutorial
from .models import Reaccion
# Register your models here.
admin.site.register(Tutorial)
admin.site.register(Reaccion)