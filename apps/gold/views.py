from django.shortcuts import render, redirect
import random
from django.utils.timezone import datetime

def index(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, "gold/index.html")

def getMoney(request):
    time = str(datetime.now())
    loose = None
    if request.POST['building'] == 'farm':
        coins = random.randrange(10, 21)
        request.session['gold'] += coins
        request.session['activity'].insert(0, (coins, "farm", time, loose))
    elif request.POST['building'] == 'cave':
        coins = random.randrange(5, 11)
        request.session['gold'] += coins
        request.session['activity'].insert(0, (coins, "cave", time, loose))
    elif request.POST['building'] == 'house':
        coins = random.randrange(2, 6)
        request.session['gold'] += coins
        request.session['activity'].insert(0, (coins, "house", time, loose))
    elif request.POST['building'] == 'casino':
        chance = random.randrange(0,2)
        if chance == 1:
            coins = random.randrange(0,51)
            request.session['gold'] += coins
            request.session['activity'].insert(0, (coins, "casino", time, loose))
        else:
            loose = 0
            coins = random.randrange(0,51)
            request.session['gold'] -= coins
            request.session['activity'].insert(0, (coins, "casino", time, loose))
    print ('*'*50)
    print (request.session['gold'])
    print ('*'*50)
    print ('*'*50)
    print (request.session['activity'])
    print ('*'*50)
    return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activity'] = []
    return redirect('/')
# Create your views here.
