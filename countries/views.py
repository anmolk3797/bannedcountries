from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.http import JsonResponse
from django.conf import settings
from .models import Country
import json
import os

# Create your views here.
def ajax_request(function):
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return render_to_response('error/ajax_required.html', {},
                context_instance=RequestContext(request))
        else:
            return function(request, *args, **kwargs)
    return wrapper

class AjaxGeneral(TemplateView):
    template_name= "index.html"
    def get(self, request):
        data={}
        return render_to_response(self.template_name, data,
            context_instance=RequestContext(request))

    @method_decorator(ajax_request)
    def dispatch(self, *args, **kwargs):
        return super(AjaxGeneral, self).dispatch(*args, **kwargs)

class CountryView(View):
    template_name = 'index.html'

    def get(self, request):
        country = Country.objects.all()
        if not country:
            json_data = open(os.path.join(settings.BASE_DIR, 'static/country.json'))   
            data1 = json.load(json_data) # deserialises it
            # data2 = json.dumps(data1) # json formatted string
            for data in data1:
                country = Country()
                country.code = data['code']
                country.label = data['label']
                country.phone = data['phone']
                country.save()

        country = Country.objects.all()
        banned = Country.objects.filter(is_active = True)
        return render(self.request, self.template_name, {'queryset': country, 'banned':banned})
    
    def post(self,request):
        import pdb; pdb.set_trace()
        pass


def ajax(request):
    username = request.GET.get('id', None)
    import pdb; pdb.set_trace()
    data = {
        'is_taken': Country.objects.filter(id=username).exists()
    }
    return JsonResponse(data)