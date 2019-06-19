from django.shortcuts import render,redirect
from .models import Video
from .forms import Vform

# Create your views here.
def Vdata(request):
    videos=Video.objects.order_by('-date')
    context={'videos':videos}
    return render(request,'home.html',context)


def Vrform(request):
    if request.method=='POST':
        form=Vform(request.POST)
        if form.is_valid():
            new_req=Video(title=request.POST['Name'],video_desc=request.POST['Description'])
            new_req.save()
            return redirect('home')
    else:
        form=Vform()


    context={'form':form}






    return render(request,'form.html',context)
