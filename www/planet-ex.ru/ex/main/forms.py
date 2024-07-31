from django.forms import ModelForm, TextInput, NumberInput
from .models import orders

class ordersForm(ModelForm):
    class Meta:
        model = orders
        fields = ['name', 'tel', 'comments']

        widgets = {

            'name': TextInput(attrs={

                'class': "Djinput",
                'placeholder': 'Имя'
            }),


            'tel': TextInput(attrs={

                'class': "Djinput",
                'placeholder': 'Телефон'
            }),

            'comments': TextInput(attrs={

                'class': "Djtextarea",
                'placeholder': 'Комментарий'
            }),


        }


