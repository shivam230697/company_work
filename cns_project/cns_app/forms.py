from django import forms
from .models import RawMaterialModel, ProductionModel, FinalGoods


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


class FinalGoodsForm(forms.ModelForm):
    class Meta:
        model = FinalGoods
        fields = "__all__"
