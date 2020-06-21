from django.db import models
from django.contrib.auth.models import User
from datetime import datetime as dt, timedelta
from django.utils import timezone

#   model class for wallet
class Wallet(models.Model) : 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    description = models.CharField(max_length=200, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now())

    def __str__(self) : 
        return self.name


#   model class for transaction
class Transaction(models.Model) : 

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_linked = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(default = timezone.now())
    

    def __str__(self) : 
        return self.title