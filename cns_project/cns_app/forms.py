import uuid

from django import forms
from .models import RawMaterialModel, ProductionModel, InvoiceModel, Customer, PaymentModel
from address.forms import AddressField
from localflavor.in_.forms import INStateSelect


class IndexForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()


class RawMaterialForm(forms.ModelForm):
    class Meta:
        model = RawMaterialModel
        fields = "__all__"


class ProductionForm(forms.ModelForm):
    class Meta:
        model = ProductionModel
        fields = "__all__"

    class Media:
        js = ('js/auto_capitalize.js',)


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class InvoiceForm(forms.Form):
    from .environment import Environment
    invoice_env = Environment()
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())

    total = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    gst = forms.IntegerField()
    discount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    payment = forms.DecimalField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    item45mm = forms.BooleanField(label='Item 1', required=False,
                               widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    item90mm = forms.BooleanField(label='Item 2', required=False,
                               widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    item_pencil = forms.BooleanField(label='Item 3', required=False,
                               widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    quantity_item1 = forms.IntegerField(label='Quantity for Item 1', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price_item1 = forms.DecimalField(label='Price for Item 1', required=False,
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))

    quantity_item2 = forms.IntegerField(label='Quantity for Item 2', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price_item2 = forms.DecimalField(label='Price for Item 2', required=False,
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))

    quantity_item3 = forms.IntegerField(label='Quantity for Item 3', required=False,
                                        widget=forms.NumberInput(attrs={'class': 'form-control'}))
    price_item3 = forms.DecimalField(label='Price for Item 3', required=False,
                                     widget=forms.NumberInput(attrs={'class': 'form-control'}))
    shipping_address = forms.CharField(max_length=50)
    shipping_state = forms.ChoiceField(choices=invoice_env.STATE_CHOICES, label="Shipping State")
    shipping_city = forms.CharField(max_length=20)
    shipping_zip_code = forms.IntegerField()


class CustomerForm(forms.Form):
    from .environment import Environment
    state_env = Environment()
    customer_name = forms.CharField()
    customer_number = forms.IntegerField()
    customer_address = forms.CharField()
    customer_state = forms.ChoiceField(choices=state_env.STATE_CHOICES)
    customer_city = forms.CharField(max_length=20)
    zip_code = forms.IntegerField(label='ZIP Code')
    # payment_status = forms.ChoiceField(choices=[('pending', 'PENDING'), ('paid', 'PAID')])
    # payment_dues = forms.DecimalField()


class PaymentForm(forms.Form):
    p_method = (
        ('cash', 'cash'),
        ('online', 'online'),
    )
    p_status = (
        ('paid', 'paid'),
        ('pending', 'pending'),
    )
    customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    payment_method = forms.ChoiceField(choices=p_method, label='payment method')
    payment_amount = forms.DecimalField()
    # payment_status = forms.ChoiceField(choices=p_status, label='Status')
    # payment_dues = forms.DecimalField(null=True, max_digits=12, editable=False, decimal_places=2)
