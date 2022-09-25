from django.http import HttpResponse
from django.db.models import Count, Q
from django.template import loader
from .models import Catalogues
import datetime
#from django.shortcuts import render
#from django.db.models import Q
from django.views.generic import ListView

today = datetime.date.today()
thisyear = datetime.date.today().year
thismonth = datetime.date.today().month

def index(request):
    
    mycatalogue = Catalogues.objects.all().values()
    bookcount = Catalogues.objects.all().count()
    pubyear = Catalogues.objects.values('publish_year').order_by('-publish_year').annotate(pubyearcount=Count('publish_year'))
    typepub = Catalogues.objects.values('publisher_type').annotate(typepubcount=Count('publisher_type'))
    typegenre = Catalogues.objects.values('genre').annotate(typegenrecount=Count('genre'))
    lang = Catalogues.objects.values('language').annotate(langcount=Count('language'))
    subj =Catalogues.objects.values('subject').annotate(subjcount=Count('subject'))
    typeaut = Catalogues.objects.values('authorship_type').annotate(typeautcount=Count('authorship_type'))
        
    catyear = Catalogues.objects.filter(entry_date__year=thisyear).count()
    catmonth = Catalogues.objects.filter(entry_date__month=thismonth).count()
    catt = Catalogues.objects.filter(entry_date=today).count()
    
    context = {
        'mycatalogue' : mycatalogue,
        'pubyear' : pubyear,
        'typepub' : typepub,
        'typegenre' : typegenre,
        'lang' : lang,
        'subj' : subj,
        'typeaut' : typeaut,          
        'bookcount' : bookcount,
        'catyear' : catyear,
        'catt' : catt,
        'catmonth' : catmonth,
      }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


def detail_pubyear(request, publish_year):
    detail_pubyear = Catalogues.objects.all().filter(publish_year=publish_year)
    template = loader.get_template('detail_publishyear.html')
    context = {
    'detail_pubyear' : detail_pubyear,
  }
    return HttpResponse(template.render(context, request))

def detail_publisher(request, publisher_type):
  detail_pub = Catalogues.objects.all().filter(publisher_type=publisher_type)

  template = loader.get_template('detail_publisher.html')
  context = {
    'detail_pub' : detail_pub,
  }
  return HttpResponse(template.render(context, request))


def detail_genre(request, genre):
  detail_genre = Catalogues.objects.all().filter(genre=genre)

  template = loader.get_template('detail_genre.html')
  context = {
    'detail_genre' : detail_genre,
  }
  return HttpResponse(template.render(context, request))

def detail_language(request, language):
  detail_language = Catalogues.objects.all().filter(language=language)

  template = loader.get_template('detail_language.html')
  context = {
    'detail_language' : detail_language,
  }
  return HttpResponse(template.render(context, request))

def detail_subject(request, subject):
  detail_subject = Catalogues.objects.all().filter(subject=subject)

  template = loader.get_template('detail_subject.html')
  context = {
    'detail_subject' : detail_subject,
  }
  return HttpResponse(template.render(context, request))


def detail_authorship(request, authorship_type):
  detail_aut = Catalogues.objects.all().filter(authorship_type=authorship_type)

  template = loader.get_template('detail_authorship.html')
  context = {
    'detail_aut': detail_aut,
  }
  return HttpResponse(template.render(context, request))


class SearchResultsView(ListView):
    model = Catalogues
    template_name = 'search_result.html'

    def get_queryset(self):
        query1 = self.request.GET.get('q1')
        query2 = self.request.GET.get('q2')
        object_list = Catalogues.objects.filter(
          Q(entry_date__gte=query1)&Q(entry_date__lte=query2)
    

            )
        return object_list