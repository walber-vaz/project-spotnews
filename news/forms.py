from django import forms

from .models import News


class CategoryForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=200)


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = [
            'title',
            'content',
            'author',
            'created_at',
            'image',
            'categories',
        ]
        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'created_at': forms.DateInput(attrs={'type': 'date'}),
            'author': forms.Select(),
        }

        # tranformar autor em select


# class NewsForm(forms.Form):
#     title = forms.CharField(label='Título', max_length=200)
#     content = forms.CharField(label='Conteúdo', widget=forms.Textarea)
#     author = forms.ModelChoiceField(
#         label='Autoria', queryset=News.objects.all()
#     )
#     created_at = forms.DateField(
#         label='Criado em', widget=forms.DateInput(attrs={'type': 'date'})
#     )
#     image = forms.ImageField(label='URL da Imagem', required=False)
#     category = forms.ModelChoiceField(
#         label='Categorias',
#         queryset=Categories.objects.all(),
#         widget=forms.CheckboxSelectMultiple,
#     )
