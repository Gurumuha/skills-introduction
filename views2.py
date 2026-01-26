#template loaders
from django http import HttpResponse 
from django.template import loader
#sending requests

def rocky (request):
  template =loader.get_template('rockyhome.html')
  return HttpResponse (template.render())
  
