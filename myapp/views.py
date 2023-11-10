from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpRequest,HttpResponse

#List object
posts = [
        {
            'Name' : 'john',
             'tittle' : 'Info1',
             'Number' : '999xxxxx110'
        },
        {
            'Name' : 'sam',
            'tittle' : 'Info2',
             'Number' : '998xxxxx110'
        }
    ]


# Create your views here.
def myfunc(request):
    return render(request,'blog/about.html',{'title':'about blog'})

def myfunc2(request):
    context = {
        'poster' : posts
    }
    return render(request,'blog/index.html',context)