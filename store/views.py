from django.shortcuts import render
from .models import Store
# Create your views here.
def home(request):
	return render(request, 'home.html')

def list_stores(request):
	stores = Store.objects.all();
	return render(request,'list_stores.html',{'stores':stores});