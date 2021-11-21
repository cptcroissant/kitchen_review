from django import forms

CHOICES = [('1', 1), ('2', 2)]


class NameForm(forms.Form):

    """# f_name = forms.CharField(label='First_name', max_length=100)
    sl = forms.FloatField(label='sepal length', min_value=0)
    sv = forms.FloatField(label='sepal width', min_value=0)
    pl = forms.FloatField(label='petal length', min_value=0)
    pw = forms.FloatField(label='petal width', min_value=0)
    # choice = forms.ChoiceField(widget=forms.Select, choices=CHOICES)"""

    input_text = forms.CharField(label='Впиши текст сюда', max_length=300)
