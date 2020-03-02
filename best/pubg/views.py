from django.shortcuts import render, redirect
from .models import Match, Join, Links
from django.contrib import messages
from datetime import date

# Create your views here.

def index(request):
    matches = Match.objects.all()
    no_of_cards = len(matches)
    abc = matches[::-1]
    link = Links.objects.all()
    today = date.today()
    print(today)
    
    params = {'match': abc, 'range':range(0, no_of_cards), 'link':link, 'today':today}
    return render(request, 'index.html', params)


def mdview(request, myid):
    # fetching the matches using id
    match = Match.objects.filter(id=myid)
    # print(match)
    join = Join.objects.filter(Match_id=myid)
    # print(join)
    joined = len(join)
    return render(request, 'mdview.html', {'match':match[0],'myid':myid, 'join':join, 'joined':joined})


def tandc(request):
    return render(request, 'terms.html')


def joinnow(request):
    
    username = request.POST['username']
    pubg_id = request.POST['pubg_id']
    Match_id = request.POST['match_id']
    match_name = request.POST['match_name']
    pubg_name = request.POST['pubg_name']
    
    if Join.objects.filter(username=username, Match_id=Match_id).exists():
         messages.info(request, 'pass not matching...')

    else:
        join = Join(username=username, pubg_id=pubg_id, pubg_name=pubg_name, Match_id=Match_id, match_name=match_name)
        join.save();
    return redirect('/')




def asd(request):
    return render(request, 'login.html')