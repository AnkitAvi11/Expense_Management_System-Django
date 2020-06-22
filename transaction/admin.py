from django.contrib import admin

# Register your models here.

from .models import Wallet, Transaction

class TransactionAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'title', 'amount', 'date', 'transaction_type')
    list_display_links = ('id', 'title')
    
class WalletAdmin(admin.ModelAdmin) : 
    list_display = ('id', 'name', 'description', 'total_amount', 'user', 'date_created')
    list_display_links = ('id', 'name')

admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
