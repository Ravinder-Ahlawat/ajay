from django.shortcuts import render, redirect
from .models import Match, Join

# Create your views here.

def index(request):
    matches = Match.objects.all()
    no_of_cards = len(matches)
    params = {'match': matches, 'range':range(0, no_of_cards)}
    return render(request, 'index.html', params)


def mdview(request, myid):
    # fetching the matches using id
    match = Match.objects.filter(id=myid)
    join = Join.objects.filter(Match_id=myid)
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

    join = Join(username=username, pubg_id=pubg_id, pubg_name=pubg_name, Match_id=Match_id, match_name=match_name)
    join.save();
    return redirect('/')
