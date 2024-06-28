from django.contrib import admin

from .models import Properties, Renter, Transaction
# Register your models here.

admin.site.register(Properties)
admin.site.register(Renter)
admin.site.register(Transaction)


