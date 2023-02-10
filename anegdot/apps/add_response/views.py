from django.shortcuts import render
from .models import Offer
from .forms import OfferForm
from anecdote.forms import AnecdoteForm

def index(request):
    if request.method == "POST":
        form = OfferForm(request.POST)
        if form.is_valid():
            form.save()
    if request.method == "POST":
        push = AnecdoteForm(request.POST)
        if push.is_valid():
            push.save()

    form = OfferForm()
    push = AnecdoteForm()
    
    data = {
        'form': form,
        'push': push
    }
    
    return render(request, 'poll/index.html', data)

def offers(request):
    offers_list = Offer.objects.all()
    return render(request, 'poll/offers.html', {'offers_list': offers_list})
