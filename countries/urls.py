from django.urls import path, include
from django.views.generic import TemplateView
from .views import AjaxGeneral, CountryView, ajax

urlpatterns = [
    # path("", TemplateView.as_view(template_name="index.html")),
    path('',CountryView.as_view()),
    path('ajax/', ajax, name='ajax'),

]