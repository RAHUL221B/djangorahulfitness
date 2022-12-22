from django import forms
from .models import Post, Category

# choices = [('fatloss','fatloss'), ('training','training'), ('abs','abs'), ('nutrition','nutrition')]
choices = Category.objects.all().values_list('name','name')

choice_list =[]

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','snippet','content','author','category','timestamp','header_image')

        widgets = {
            'title' : forms.TextInput(attrs =  {'class': 'form-control'}),
            'title_tag' : forms.TextInput(attrs = {'class': 'form-control'}),
            'content' : forms.Textarea(attrs = {'class': 'form-control'}),
            'author' : forms.TextInput(attrs = {'class': 'form-control'}),
            'category' : forms.Select(choices = choice_list,attrs = {'class': 'form-control'}),
            'timestamp' : forms.DateInput(attrs = {'type': 'date'}),
             'snippet'  : forms.Textarea(attrs = {'class': 'form-control'}),
        }
