from django import forms


class CrudForm(forms.Form):
    id = forms.IntegerField(label="id:")
    name = forms.CharField(label="name:", max_length=200)
    address = forms.CharField(label="address", max_length=200)
