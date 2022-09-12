from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import contactform



def myview(request):
    return HttpResponse('<h1>this is first function view</h>')


class Myview(View):

    def get(self, request):
     return HttpResponse('<h1>this is first class based view</h>')


class Amit(Myview):

    def get(self, request):
        return HttpResponse('<h1> amit is great person</<h1>') 
        Myview()    

def contactfun(request):
    if request.method == 'POST':
        form = contarctform(request.POST)
        if form.is_vaild():
            print(form.cleaned_date['name'])
            return HttpResponse('thanks for giving informantion!!')
        else:
            form = contactform()
        return render((request), 'class_view/', {'form': form})    



