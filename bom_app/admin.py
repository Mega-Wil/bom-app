from django import forms
from django.contrib import admin

from .models import Product, BOMItem

# Register your models here.
admin.site.register(Product)
admin.site.register(BOMItem)

class BOMItemForm(forms.ModelForm):
    class Meta:
        model = BOMItem
        fields = ['parent', 'component', 'quantity']