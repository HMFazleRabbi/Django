from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse('<p> Home View</p>')

def pet_detail(request, pet_id):
    return HttpResponse(f"<p> Pet Details with id {pet_id}</p>")