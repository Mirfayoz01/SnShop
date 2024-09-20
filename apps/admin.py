from django.contrib import admin
from .models import *
admin.site.register(Person)
admin.site.register(Product)
admin.site.register(About)
admin.site.register(Home)
admin.site.register(contact)
admin.site.register(Users)


@admin.register(Registered_user)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'company')
