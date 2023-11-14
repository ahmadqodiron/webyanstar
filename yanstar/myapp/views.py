from django.http import HttpResponse
from django.template import loader

def myapp(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def product(request):
  template = loader.get_template('product.html')
  return HttpResponse(template.render())

def aboutme(request):
  template = loader.get_template('aboutme.html')
  return HttpResponse(template.render()) 