from django.shortcuts import render
from .models import Match

# Create your views here.

def index(request):
    matches = Match.objects.all()
    print(matches)
    no_of_cards = len(matches)
    params = {'match': matches, 'range':range(0, no_of_cards)}
    return render(request, 'index.html', params)