from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from parler.models import TranslatableModel, TranslatedFields
from parler.forms import TranslatableModelForm, TranslatedField
from parler.utils.context import switch_language

from .forms import CreateNewResource, AddLangauges

from .models import Resource

    
def get_newresource(request):
    form = ""
    if request.method == 'POST':
        form = CreateNewResource(request.POST)
        if form.is_valid():
            t = form.cleaned_data["title_text"]
            d = form.cleaned_data["description"]
            u = form.cleaned_data["url"]
            lv = form.cleaned_data["level"]
            kc = form.cleaned_data["key_competence"]
            r = Resource(title_text = t, description = d, url = u, level = lv, key_competence = kc)
            r.save()
            q = form.cleaned_data["other_lang"]
            if q:
                return HttpResponseRedirect('/'+r.get_current_language()+'/%s/newlang/' %r.id)
#             t_i = form.cleaned_data["title_text_it"]
#             d_i = form.cleaned_data["description_it"]
#             r.set_current_language('it')
#             r.title_text = t_i
#             r.description = d_i
#             r.save()
            else:
                return HttpResponseRedirect('/%s/thanks/' %r.id)
    else:
        form = CreateNewResource()
#         r = Resource(title_text = "chatch22", description = "why are you not set up as post?")
#         r.save()
    return render(request, 'newresource.html', {'form': form})    
    
    
class ListResource(generic.ListView):
    model = Resource
    template_name = 'index.html'
    context_object_name = 'forms'
	    
	    
class DetailView(generic.DetailView):
    model = Resource
    template_name = 'resourceview.html'
   #  def get_queryset(self):
#         """
#         Excludes any questions that aren't published yet.
#         """
#         return Resource.objects.filter(pub_date__lte=timezone.now())

class Thanks(generic.DetailView):
	model = Resource
	template_name = 'thanks.html'
    
def newlang(request, pk):
    form = ""
    if request.method == 'POST':
        form = AddLangauges(request.POST)
        if form.is_valid():
            t1 = form.cleaned_data["title_text1"]
            d = form.cleaned_data["description1"]
            l = form.cleaned_data["language1"]
            u = form.cleaned_data["url1"]
            r = Resource.objects.get(id=pk)
            r.set_current_language(l)
            r.title_text = t1
            r.description = d
            r.url = u
            r.save()
            t2 = form.cleaned_data["title_text2"]
            t3 = form.cleaned_data["title_text3"]
            if t2:
                d = form.cleaned_data["description2"]
                l = form.cleaned_data["language2"]
                u = form.cleaned_data["url2"]
                r.set_current_language(l)
                r.title_text = t2
                r.description = d
                r.url = u
                r.save()                
            if t2:
                d = form.cleaned_data["description3"]
                l = form.cleaned_data["language3"]
                u = form.cleaned_data["url3"]
                r.set_current_language(l)
                r.title_text = t3
                r.description = d
                r.url = u
                r.save()   
            return HttpResponseRedirect('/%s/thanks/' %r.id)
    else:
        form = AddLangauges()
#         r = Resource(title_text = "chatch22", description = "why are you not set up as post?")
#         r.save()
    return render(request, 'newlang.html', {'form': form, 'pk':pk})    
