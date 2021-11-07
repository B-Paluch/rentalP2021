from django import forms
from .models import RentItem

# formularz do dodawania przedmiotu
class ItemCreateForm(forms.ModelForm):
    class Meta:
        model = RentItem
        exclude = ['rentState', 'name', 'surname', 'rentDate']


# formularz do update przedmiotu (wypozyczenia)
class RentItemForm(forms.ModelForm):
    class Meta:
        model = RentItem
        exclude = ['rentItemName', 'rentState']
