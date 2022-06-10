from django.contrib import admin
from .models import Model, Deep_Learning, Processing, Operations, Public, Custom
# Register your models here.

class GameAdmin(admin.ModelAdmin):
    pass
admin.site.register(Model)
admin.site.register(Processing)
admin.site.register(Deep_Learning)
admin.site.register(Operations)
admin.site.register(Public)
admin.site.register(Custom)
