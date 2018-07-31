from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse_lazy
def RegisterView(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if(form.is_valid):
            form.save()
            return HttpResponseRedirect(reverse_lazy('reg_success'))
    else:
        form=UserCreationForm()
        args={
            'form':form,
        }
        return render(request, 'registration/reg_form.html',args)

def RegSuccessView(request):
    return render(request,'registration/reg_success.html')