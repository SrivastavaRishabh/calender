from django.shortcuts import render,get_object_or_404
from .models import Entry
from .forms import Entryform
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    entries=Entry.objects.all()
    return render(request,'calapp/index.html',{'entries':entries})

def details(request,pk):
    entry=Entry.objects.get(id=pk)
    return render(request,'calapp/details.html',{'entry':entry})
def add(request):
    if request.method=='POST':
        form=Entryform(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            date=form.cleaned_data['date']
            description=form.cleaned_data['description']

            Entry.objects.create(
                name=name,
                date=date,
                description=description,
            ).save()

            return HttpResponseRedirect('/')

    else:
        form=Entryform()
    return render(request,'calapp/form.html',{'form':form})
def delete(request,pk):
        if request.method=='DELETE':
            entry=get_object_or_404(Entry,pk=pk)
            entry.delete()
        return HttpResponseRedirect('/')


