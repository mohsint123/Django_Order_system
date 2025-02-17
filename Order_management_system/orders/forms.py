from django import forms
from .models import Order, FoodItem

class OrderForm(forms.ModelForm):
    items = forms.ModelMultipleChoiceField(
        queryset=FoodItem.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Order
        fields = ['table_number', 'status', 'items']
        labels = {
            'table_number': 'Table Number',
            'status': 'Status',
            'items': 'Select Items'
        }
        widgets = {
            'table_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
