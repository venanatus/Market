import os
from django import forms
from .models import *


class OrderForm(forms.ModelForm):
    address = forms.CharField(label='Address')
    phone = forms.CharField(label='Phone')

    class Meta:
        model = User
        fields = ['address', 'phone']


class BaseForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input has-text-centered'}), label='Введите название')
    description = forms.CharField(widget=forms.Textarea(), label='Опишите ваш продукт')
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input has-text-centered'}), label='Цена')
    preview = forms.ImageField(widget=forms.FileInput(attrs={'class': 'input has-text-centered'}), label='Главное фото')
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    subcategory = forms.ModelChoiceField(queryset=SubCategory.objects.all())
    package_length = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '3',
                                        'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}),
        label='Длина упаковки')
    packing_width = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '3',
                                        'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}),
        label='Ширина упаковки')
    packing_height = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input has-text-centered', 'maxlength': '3',
                                        'oninput': 'javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength)'}),
        label='Высота упаковки')
    made_country = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}),
                                   label='Введите название место произдоства')
    equipment = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Комплектация')

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'preview', 'category', 'subcategory', 'package_length',
                  'packing_width', 'packing_height', 'made_country', 'equipment']


class ImageForm(forms.ModelForm):
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()

    class Meta:
        model = Image
        fields = ['image1', 'image2', 'image3', 'image4']


class OrderForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Введите Адрес')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Введите Номер Телефона')

    class Meta:
        model = User
        fields = ['address', 'phone']
