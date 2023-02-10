from django.forms import ModelForm, Textarea
from .models import Offer

class OfferForm(ModelForm):
    class Meta:
        model = Offer
        fields = ['offer_text']
        
        widgets = {
            'offer_text': Textarea(attrs={
                'placeholder': 'Пропозиція або питання'
            })
        }
