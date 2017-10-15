from django import forms
from book_shop_app.models import Customer, Employee, Order, PublishingHouse, Comment, Book, MoreAboutOrder
import re
from django.core.exceptions import ValidationError


class PublishingHouseForm(forms.ModelForm):

    email = forms.EmailField()

    def clean_tel(self):
        data = self.cleaned_data['tel']
        if not re.match(r'(\+?\d[- .]*){7,13}$', data):
            raise ValidationError('Введите корректный телефон')

        return data

    class Meta:
        model = PublishingHouse
        fields = '__all__'

        labels = {
            'name': ('Название'),
            'email': ('E-mail'),
            'tel': ('Телефон'),
        }


class CustomerForm(forms.ModelForm):

    def clean_fio(self):
        data = self.cleaned_data['fio']
        if not re.match(r'[\-\.,A-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное ФИО')

        return data

    def clean_address(self):
        data = self.cleaned_data['address']
        if not re.match(r'[0-9A-Za-zА-Яа-яЁё\-\.\/\s]+$', data):
            raise ValidationError('Введите корректный адрес')

        return data

    def clean_tel(self):
        data = self.cleaned_data['tel']
        if not re.match(r'(\+?\d[- .]*){7,13}$', data):
            raise ValidationError('Введите корректный телефон')

        return data

    class Meta:
        model = Customer
        fields = '__all__'

        labels = {
            'fio': ('ФИО'),
            'address': ('Адрес'),
            'tel': ('Телефон'),
        }

        widgets = {
            'fio': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'tel': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'pattern': '(\+?\d[- .]*){7,13}'})
        }


class BookForm(forms.ModelForm):

    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'[\-\.,\dA-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное название')

        return data

    def clean_year(self):
        data = self.cleaned_data['year']
        if data < 0 or data > 2017:
            raise ValidationError('Введите корректный год')

        return data
    
    def clean_price(self):
        data = self.cleaned_data['price']
        if data <= 0:
            raise ValidationError('Введите корректную цену')

        return data
    
    def clean_count(self):
        data = self.cleaned_data['count']
        if data <= 0:
            raise ValidationError('Введите корректное количество')

        return data

    def clean_author(self):
        data = self.cleaned_data['author']
        if not re.match(r'[\-\.,A-Za-zА-Яа-яЁё\s]+$', data):
            raise ValidationError('Введите корректное имя автора')

        return data

    class Meta:
        model = Book
        fields = '__all__'

        labels = {
            'name': ('Название'),
            'author': ('Автор'),
            'subject': ('Жанр'),
            'publishing_house': ('Издательство'),
            'year': ('Год'),
            'price': ('Цена'),
            'count': ('Количество'),
            'image': ('Обложка'),
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'subject': forms.Select(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'publishing_house': forms.Select(attrs={'class':'form-control', 'aria-describedby':'basic-addon1'}),
            'year': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number'}),
            'price': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number', 'step':'0.01'}),
            'count': forms.TextInput(attrs={'class':'form-control', 'aria-describedby':'basic-addon1', 'type':'number'}),
            'image': forms.FileInput(attrs={'class':'form-control btn btn-default', 'aria-describedby':'basic-addon1'})
        }