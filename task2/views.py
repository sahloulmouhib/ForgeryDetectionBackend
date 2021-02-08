from task2.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse
from .models import Client
from django.shortcuts import render
from .forms import ReviewForm
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from .tasks import sleepy

#def handle_uploaded_file(f):   
 #   with open('media/images/'+f.name, 'wb+') as destination:   
  #      for chunk in f.chunks(): 
   #         destination.write(chunk)  
def home_view(request):
    return render(request , "index.html")

def client_view(request) :
    my_form=ReviewForm()
    if request.method =='POST' :
        my_context={'form':my_form}
        my_form=ReviewForm(request.POST, request.FILES)
        if my_form.is_valid():
            #handle_uploaded_file(request.FILES["image"])
            #uploaded_file=request.FILES['image']
            #print(uploaded_file.name)            
            #fs.save(uploaded_file.name,uploaded_file)
            #fs=FileSystemStorage()
            name=my_form.cleaned_data['firstName']
            email=my_form.cleaned_data['email']
            print(my_form.cleaned_data['image'])
            send_mail("Thank you "+name+" for using Detectify","hello,you will recieve the real image once we complete processing it ","sahloulmouhib92@gmail.com",[email])
            client=Client.objects.create(**my_form.cleaned_data)
            print (client.id)
            #sleepy.delay(client.id)
            return render(request , "waiting.html",my_context)
        else:
            
            print(my_form.errors)    
    my_context={'form':my_form}
    return render(request , "review.html",my_context)



    