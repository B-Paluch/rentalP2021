from django import forms
from django.forms import formset_factory

from .models import RentItem

# formularz do dodawania przedmiotu
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = RentItem
        exclude = ['rentState', 'name', 'surname', 'rentDate', 'id']

class ItemCreateMultiForm(forms.Form):
    name = forms.CharField(
        label='nazwa przedmiotu',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'podaj nazwę przedmiotu'
        })
    )

ItemCreateFormset = formset_factory(ItemCreateMultiForm, extra=1)


# formularz do update przedmiotu (wypozyczenia)
class RentItemForm(forms.ModelForm):
    class Meta:
        model = RentItem
        exclude = ['rentItemName', 'rentState', 'id']
