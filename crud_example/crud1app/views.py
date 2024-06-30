from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .forms import RCForm
from .models import RunCodes

# Create your views here.
def create_view(request):
    form = RCForm()
    if request.method == 'POST':
        form= RCForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request,'create_view.html',{'form':form})
    
def retrieve_list(request):
    obj = {}
    obj['data'] = RunCodes.objects.all()
    return render(request,'retrieve_list.html',context=obj)

def retrieve_detail(request,id):
     obj = {}
     obj['data']=RunCodes.objects.get(id=id)
     return render(request,'retrieve_detail.html',context=obj)

def update_view(request):
    obj=get_object_or_404(RunCodes,id=id)
    form=RCForm()
    form = RCForm(request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    return render(request,'update_view',{'form':obj})

def delete_view(request):
    obj=get_object_or_404(RunCodes,id=id)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/')
    return render(request,'delete_view')

    


