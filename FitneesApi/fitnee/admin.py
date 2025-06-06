from django.contrib import admin
from .models import BookSlot,Register




# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password', 'conf_password')
    search_fields = ('username', 'email')

admin.site.register(Register, RegisterAdmin)




class BookSlotAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'client_name', 'client_email', 'slottype','trainee','date', 'time', 'created_at')
    search_fields = ('client_id', 'client_name', 'client_email', 'slottype','trainee' ,'date', 'time')

admin.site.register(BookSlot, BookSlotAdmin)