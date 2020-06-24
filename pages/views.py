from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from userprofile.decorators import is_admin
from django.core.paginator import Paginator

from transaction.models import Wallet, Transaction

def indexView(request) : 
    if request.user.is_authenticated : 
        return redirect('/profile/dashboard/')
    else : 
        return render(request, 'pages/home.html')

def aboutview(request) : 
    return HttpResponse('about page')

#   view function for the 
@login_required(login_url='/account/login/')
@is_admin
def transactions_page(request) : 
    user_wallets = Wallet.objects.filter(user__username__exact=request.user.username)
    latest_transaction = Transaction.objects.all().order_by('-date')[:10]
    context = {
        "wallets" : user_wallets,
        "transaction" : latest_transaction
    }
    return render(request, 'account/transact.html', context)

@login_required(login_url='/account/login')
@is_admin
def newwallet(request) : 
    return render(request, 'account/createwallet.html', )

@login_required(login_url='/account/login')
@is_admin
def alltransction(request) : 
    user = request.user
    transactions = Transaction.objects.all().order_by('-date')
    paginator = Paginator(transactions, 10)
    page = request.GET.get('page')
    current_page = paginator.get_page(page)
    context = {
        'transactions' : current_page
    }
    return render(request, 'account/transactionall.html', context)
