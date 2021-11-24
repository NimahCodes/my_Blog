from django.shortcuts import render, redirect
# from django.contrib.aut
from .form import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"mysite/confirmation.html")
    else:
        form= UserRegistrationForm()
        return render(request,"mysite/register.html", {'forms':form})