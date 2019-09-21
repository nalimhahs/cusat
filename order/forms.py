from django import forms
from .models import Order

class OrderForm(forms.ModelForm):

    class Meta:

        model = Order
        fields = ('waste_type', 'weight', 'pickup_date')
        widgets = {
            'pickup_date': forms.DateInput(attrs={'class': 'datetime-input'}),
        }