from django.shortcuts import render , redirect
from django.contrib import messages





from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Account created ')
            return redirect('home')
    else:    
        form =UserCreationForm()
    return render(request,'user/register.html',{'form':form} )
    


