import time
from django.http import HttpResponse
from django.shortcuts import render
import requests 
from django.core.paginator import Paginator
from . utils import Red
from rest_framework.decorators import api_view



# Create your views here.
def index(request):
    return render(request,'index.html')

@api_view(['GET'])
def search(request):
    term = request.GET.get('term')
    order = request.GET.get('order')
    sort = request.GET.get('sort')
    url = f"https://api.stackexchange.com/2.3/search/advanced?order={order}&sort={sort}&q={term}&site=stackoverflow"

    
    try:
        cache_data = Red.get(url)
    except:
        cache_data = None
    
    
    if cache_data != None:
        p = Paginator(cache_data["items"], 5)
        page = request.GET.get('page')
        current_page = p.get_page(page)
        current_page_data = p.page(int(page))
        # print("Cached Data")
        return render(request,'index.html',{'res':current_page_data,'pgs':current_page,'tm':term,'ord':order,'srt':sort})
    
    time.sleep(1)
    
    res = requests.get(url).json()

    #Cache the data
    cache_data = Red.set(url,res)
  
    p = Paginator(res["items"], 5)
    page = request.GET.get('page')

    current_page = p.get_page(page)

    
    current_page_data = p.page(int(page))
   
    return render(request,'index.html',{'res':current_page_data,'pgs':current_page})

def page(request):
    term = request.GET.get('term')
    order = request.GET.get('order')
    sort = request.GET.get('sort')
    url = f"https://api.stackexchange.com/2.3/search/advanced?order={order}&sort={sort}&q={term}&site=stackoverflow"

    
    cache_data = Red.get(url)
    
    if cache_data:
        p = Paginator(cache_data["items"], 5)
        page = request.GET.get('page')
        current_page = p.get_page(page)
        current_page_data = p.page(int(page))
        print("Cached Data")
        return render(request,'index.html',{'res':current_page_data,'pgs':current_page,'tm':term,'ord':order,'srt':sort})
    else:
        return HttpResponse('Oops')

def limit(request):
    return render(request,'limit.html')
    
    
    
