from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from userprofile.decorators import is_admin
from django.http import Http404, HttpResponse, JsonResponse

from django.contrib import messages

from .models import Wallet, Transaction
from django.utils import timezone
from datetime import timedelta, datetime as dt

@login_required(login_url='/account/login/')
@is_admin
def addWallet(request) : 
    if request.method == 'POST' : 
        user = request.user
        name = request.POST.get('wname')
        description = request.POST.get('desc')
        amount = request.POST.get('amount')
        date_created = timezone.now()
        #   creating a new wallet
        wallet = Wallet(user=user, name=name, description=description, total_amount=amount, date_created=date_created)
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
            date = timezone.now()
            user = request.user 

            transaction = Transaction(user=user, wallet_linked=wallet, title=title, description=desc, amount=amount, transaction_type=t_type, date=date)
            transaction.save()
            messages.success(request, 'Transaction added successfully')
            return redirect('/transaction/')
        except Wallet.DoesNotExist : 
            messages.error(request, 'That wallet has been deleted')
            return redirect('/transaction/')


@login_required(login_url='/account/login/')
@is_admin
def bargraph(request) : 
    from django.core import serializers
    start_date = timezone.now() - timedelta(days=6)
    end_date = timezone.now()
    transactions = serializers.serialize('json', Transaction.objects.filter(user=request.user, date__range=(start_date, end_date)))
    data_send = {
        "start_date" : start_date,
        "end_date" : end_date,
        "transactions" : transactions
    }
    return JsonResponse(data_send, safe=False)

@login_required(login_url='/account/login/')
@is_admin
def walletSetting(request) :
    user = request.user
    wallets = user.wallet_set.all().order_by('-date_created')
    context = {
        "wallets" : wallets
    }
    return render(request, 'pages/walletsetting.html', context)


@login_required(login_url='/account/login/')
@is_admin
def getWallet(request) :
    if request.method == 'POST' : 
        from django.core import serializers
        user = request.user
        wallet_id = request.POST.get('wallet_id')
        wallet = serializers.serialize('json', Wallet.objects.filter(user=user, id=wallet_id))
        return JsonResponse(wallet, safe=False)


@login_required(login_url='/account/login/')
@is_admin
def changeWalletSetting(request) : 
    if request.method == 'POST' :
        try : 
            wallet_id = request.POST.get('wallet_id')
            user = request.user
            Wallet.objects.filter(user=user, id=wallet_id).update(name=request.POST.get('wname'), description=request.POST.get('description'))
            messages.success(request, 'Changes were saved')
            return redirect('/wallet-setting/')
        except: 
            messages.error(request, 'Some errors occurred')
            return redirect('/wallet-setting/')
    
@login_required(login_url='/account/login/')
@is_admin
def deleteWallet(request) : 
    if request.method == 'POST' : 
        user = request.user
        wallet_id = request.POST.get('wallet_id')
        wallet = Wallet.objects.get(user=user, id=wallet_id)
        wallet.delete()
        messages.success(request, 'Wallet has been deleted successfully')
        return redirect('/wallet-setting/')