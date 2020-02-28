from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from web.models import Expense,income,Token,User
from json import JSONEncoder
from datetime import datetime


@csrf_exempt
def submit_income(request):
    ## TODO: token might be fake, amount might be fake.
    this_token = request.POST['token']
    this_user= User.objects.filter(token__token = this_token).get()
    if 'date'  not in request.POST:
        date = datetime.now()

    income.objects.create(user=this_user,amount = request.POST['amount'],
    text = request.POST['text'], date = date)
    return JsonResponse({
    'status' :'ok'
    },encoder=JSONEncoder)




@csrf_exempt
def submit_expense(request):
    ## TODO: token might be fake, amount might be fake.
    this_token = request.POST['token']
    this_user= User.objects.filter(token__token = this_token).get()
    if 'date'  not in request.POST:
        date = datetime.now()

    Expense.objects.create(user=this_user,amount = request.POST['amount'],
    text = request.POST['text'], date = date)
    return JsonResponse({
    'status' :'ok'
    },encoder=JSONEncoder)
