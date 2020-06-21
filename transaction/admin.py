from django.contrib import admin

# Register your models here.

from .models import Wallet, Transaction

class TransactionAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'amount', 'date', 'transaction_type')

admin.site.register(Wallet)
admin.site.register(Transaction, TransactionAdmin)
