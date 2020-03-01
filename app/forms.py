from django import forms

class BugForm(forms.Form):
    PRIORITIES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Title', max_length=80)
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), label='Description', max_length=10000)
    priority = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=PRIORITIES)