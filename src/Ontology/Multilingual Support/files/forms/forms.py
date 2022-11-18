import datetime

from django import forms
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

LANG_CHOICES = [('en',_('English')), ('it',_('Italian')), ('de',_('German')), ('fr',_('French'))]
LEVEL_CHOICES = [('be',_('Beginner')), ('in',_('Intermediate')), ('ad',_('Advanced')), ('mu',_('Multiple'))]
KEY_COMPENCIES_CHOICES = [(1,_('Literacy')), (2,_('Multilingual')), (3,_('Mathematical, science, technology, engineering')), (4,_('Digital')), (5,_('Personal, social, learning to learn')), (6,_('Citizenship')), (7,_('Entrepreneurship')), (8,_('Cultural awareness and expression'))]


    
class CreateNewResource(forms.Form):
    title_text = forms.CharField(label=_('Title'),max_length=100)
    description = forms.CharField(label=_('Description'),max_length=200,widget=forms.Textarea)
    url = forms.URLField(label=_('url'))
    level = forms.ChoiceField(label=_('Level'),widget=forms.Select,choices=LEVEL_CHOICES)
    key_competence = forms.ChoiceField(label=_('Key Competencies'),widget=forms.Select,choices=KEY_COMPENCIES_CHOICES)
    other_lang = forms.BooleanField(label=_('Add other languages?'),required=False)
    
    
    
class AddLangauges(forms.Form):
    language1 = forms.ChoiceField(label=_('Language 1'),widget=forms.Select,choices=LANG_CHOICES)
    title_text1 = forms.CharField(label=_('Title 1'),max_length=100)
    description1 = forms.CharField(label=_('Description 1'),max_length=200,widget=forms.Textarea)
    url1 = forms.URLField(label=_('url 1'))
    language2 = forms.ChoiceField(label=_('Language 2'),widget=forms.Select,choices=LANG_CHOICES, required=False)
    title_text2 = forms.CharField(label=_('Title 2'),max_length=100, required=False)
    description2 = forms.CharField(label=_('Description 2'),max_length=200,widget=forms.Textarea, required=False)
    url2 = forms.URLField(label=_('url 2'), required=False)
    language3 = forms.ChoiceField(label=_('Language 3'),widget=forms.Select,choices=LANG_CHOICES, required=False)
    title_text3 = forms.CharField(label=_('Title 3'),max_length=100, required=False)
    description3 = forms.CharField(label=_('Description 3'),max_length=200,widget=forms.Textarea, required=False)
    url3 = forms.URLField(label=_('url 3'), required=False)
    