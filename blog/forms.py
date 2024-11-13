from django import forms
from .models import Post,Category

choices = Category.objects.all().values_list('category', 'category')

choices_list = []

for choice in choices:
    choices_list.append(choice)

class NewPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','body',]
        widgets = {
            'category' : forms.Select(choices=choices_list)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'title'})
        self.fields['title'].widget.attrs.update({'placeholder':'Title'})
        self.fields['title'].label = ''
        self.fields['body'].label = ''

class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','category','body']
        widgets = {
            'category' : forms.Select(choices=choices_list)
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class':'title'})
        self.fields['title'].widget.attrs.update({'placeholder':'Title'})
        self.fields['title'].label = ''
        self.fields['body'].label = ''