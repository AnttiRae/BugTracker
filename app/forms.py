from django import forms

class BugForm(forms.Form):
    PRIORITIES = (
        ('RED', 'High'),
        ('YELLOW', 'Medium'),
        ('GREEN', 'Low'),
    )

    title = forms.CharField(label='Title', max_length=80)
    description = forms.CharField(widget=forms.Textarea, label='Description', max_length=500)
    priority = forms.ChoiceField(choices=PRIORITIES)