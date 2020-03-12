from django.shortcuts import render, redirect
from .models import Match, Join, Links, Contact
from django.contrib import messages
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from paytm import Checksum
MERCHANT_KEY = 'kbzk1DSbJiV_O3p5'

from accounts.models import UserDetails

# Create your views here.


#Views for home page
def index(request):
    matches = Match.objects.all()
    no_of_cards = len(matches)
    abc = matches[::-1]
    link = Links.objects.all()
    today = date.today()
    params = {'match': abc, 'range':range(0, no_of_cards), 'link':link, 'today':today}
    return render(request, 'index.html', params)

# uid = 20


#for form submition
def sub2(request):
    # global uid
    uid = request.POST['id']
    path2 = request.POST['path2']
    return redirect(path2)


#for match view page
def mdview(request, myid):
    # fetching the matches using id
    match = Match.objects.filter(id=myid)
    join = Join.objects.filter(Match_id=myid)
    joined = len(join)
    # print(uid)
    # details = UserDetails.objects.filter(user_id=uid)
    # print(details)
    # request paytm to transfer the amount to your account after payment by user
    return render(request, 'mdview.html', {'match':match[0],'myid':myid, 'join':join, 'joined':joined})


#for terms and conditions page
def tandc(request):
    return render(request, 'terms.html')


def csoon(request):
    return render(request, 'comingsoon.html')


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        country = request.POST.get('country', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, country=country, desc=desc)
        contact.save()
    return render(request, 'contact.html')


# for join in a match
def joinnow(request):
    
    username = request.POST['username']
    pubg_id = request.POST['pubg_id']
    Match_id = request.POST['match_id']
    match_name = request.POST['match_name']
    pubg_name = request.POST['pubg_name']
    amount = request.POST['amount']
    Email = request.POST['email']
    uid = request.POST['uid']
    order = str(pubg_id)+str(Match_id)
    order_id = order[5:10]

    if Join.objects.filter(username=username, Match_id=Match_id).exists():
         messages.info(request, 'Already joined the match')
         a = '/mdview/' + str(Match_id)
         print(a)
         return redirect(a)


    else:
        join = Join(username=username, pubg_id=pubg_id, pubg_name=pubg_name, Match_id=Match_id, match_name=match_name, Email=Email, amount=amount)
        join.save();
        print(amount)
        if amount == '0':
            return redirect('/')
        else:
            param_dict = {

                'MID': 'WorldP64425807474247',
                'ORDER_ID': order_id,
                'TXN_AMOUNT': amount,
                'CUST_ID': Email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://64.227.29.18/handlerequest/',

            }
            param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'paytm.html', {'param_dict': param_dict})
        
            
    return redirect('/')


# User profile page
def asd(request):
    return render(request, 'login.html')


# Paytm request hanling function
@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    print(response_dict.get("RESPCODE"))
   
    return render(request, 'paymentstatus.html', {'response': response_dict})
