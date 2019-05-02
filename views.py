from django.shortcuts import render,redirect

from .models import form

def index(request):

    if request.method == 'POST':

        if request.POST.get('name') and request.POST.get('father_name'):
        
            forms = form()
            
            forms.name= request.POST.get('name')

            forms.fathername= request.POST.get('father_name')

            forms.address= request.POST.get('address')

            forms.city= request.POST.get('city')

            forms.dob= request.POST.get('birth_date')

            forms.pincode= request.POST.get('pincode')

            forms.course= request.POST.get('course')

            forms.email= request.POST.get('email')

            forms.save()

            return render(request, 'Userforms/Submit.html')
    else:
        return render(request, 'Userforms/Submit.html')
