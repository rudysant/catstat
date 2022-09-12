from django.http import HttpResponse, JsonResponse
from django.db.models import Count, Sum
from django.template import loader
from .models import Catalogues
import datetime



today = datetime.date.today()
thisyear = datetime.date.today().year
thismonth = datetime.date.today().month

def index(request):
    labels = []
    data = []
    mycatalogue = Catalogues.objects.all().values()
    typeaut = Catalogues.objects.values('authorship').annotate(typeautcount=Count('authorship'))
    
    bookcount = Catalogues.objects.all().count()
    catyear = Catalogues.objects.filter(entrydate__year=thisyear).count()
    catmonth = Catalogues.objects.filter(entrydate__month=thismonth).count()
    catt = Catalogues.objects.filter(entrydate=today).count()
    
    context = {
        'mycatalogue' : mycatalogue,
        'typeaut' : typeaut,        
        'bookcount' : bookcount,
        'catyear' : catyear,
        'catt' : catt,
        'catmonth' : catmonth,
           
    }
    
    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))


