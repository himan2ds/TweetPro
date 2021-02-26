from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweets
# Create your views here.

def home_view(request,*args,**kwargs):
    # print(args)
    return render(request,"pages/home.html",context={},status=200)
    # return HttpResponse('<h1>"Hello World"</h>')

def tweet_detail_view(request,tweet_id,*args,**kwargs):
    # print(args,kwargs)
    data={
        "id":tweet_id,
        
    }
    status=200
    try:
        obj=Tweets.objects.get(id=tweet_id)
        data['content']= obj.content
    except:
        data['message']="Not Found"
        status=404
    return JsonResponse(data,status=status)
    # return JsonResponse(f'<h1>"Hello {tweet_id} --{obj.content}"</h>')