from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from userprofile.decorators import is_admin
from django.http import Http404, HttpResponse, JsonResponse

from django.contrib import messages

from .models import Wallet, Transaction

@login_required(login_url='/account/login/')
@is_admin
def addWallet(request) : 
    if request.method == 'POST' : 
        user = request.user
        name = request.POST.get('wname')
        description = request.POST.get('desc')
        amount = request.POST.get('amount')

        #   creating a new wallet
        wallet = Wallet(user=user, name=name, description=description, total_amount=amount)
        wallet.save()
        messages.success(request, 'Wallet created succesfully!')        
        return redirect('/new-wallet/')

@login_required(login_url='/account/login/')
@is_admin
def addtransaction(request) : 
    if request.method == 'POST' :
        wallet_id = request.POST.get('wallet')
        title = request.POST.get('title')
        amount = float(request.POST.get('amount'))
        t_type = request.POST.get('type')
        desc = request.POST.get('desc')

        try : 
            wallet = Wallet.objects.get(id=wallet_id)

            user = request.user 

            transaction = Transaction(user=user, wallet_linked=wallet, title=title, description=desc, amount=amount, transaction_type=t_type)
            transaction.save()
            messages.success(request, 'Transaction added successfully')
            return redirect('/transaction/')
        except Wallet.DoesNotExist : 
            messages.error(request, 'That wallet has been deleted')
            return redirect('/transaction/')

