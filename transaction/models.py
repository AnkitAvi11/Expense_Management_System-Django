from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt, timedelta
from django.utils import timezone

#   model class for wallet
class Wallet(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=200, blank=True, null=True)
    total_amount = models.FloatField()
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.name


#   model class for transaction
class Transaction(models.Model) : 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_linked = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField()
    date = models.DateTimeField(default = timezone.now())
    
    transaction_choice = {
        ('DB' , 'DEBIT'),
        ('CR' , 'CREDIT'),
    }
    transaction_type = models.CharField(max_length=2, choices=transaction_choice, default='DB')

    def __str__(self) : 
        return self.title

    #   overriding the save method
    def save(self, *args, **kwargs) : 
        print(self.transaction_type)
        if self.transaction_type == 'DB' : 
            self.wallet_linked.total_amount -= self.amount
        else :
            self.wallet_linked.total_amount += self.amount
        self.wallet_linked.save()
        super().save(*args, **kwargs)