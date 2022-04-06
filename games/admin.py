from django.contrib import admin
from .models import Game, Game_Modes, Game_Type
# Register your models here.

admin.site.register(Game_Type)
admin.site.register(Game)
admin.site.register(Game_Modes)
