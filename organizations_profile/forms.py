from django import forms

class WithdrawForm(forms.Form):
    amount = forms.IntegerField(widget=forms.NumberInput(attrs={
        'class': 'bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-brokenwhite focus:border-green-medium',
        'min' : '0',
    }))
