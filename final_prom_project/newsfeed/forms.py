from django import forms

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control border border-2'}), max_length=100, 
                            required=True, help_text="Напишу-ка я...")
