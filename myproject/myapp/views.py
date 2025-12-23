from django.shortcuts import render
from .models import Forms
# Create your views here.

def index(request):
    return render(request,'index.html')
def forms(request):
    if request.method=='POST':
        name=request.POST.get('name',False)
        number=request.POST.get('number')
        dob=request.POST.get('dob')
        father=request.POST.get('father')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        password=request.POST.get('password')
        city=request.POST.get('city')
        address=request.POST.get('address')
        department=request.POST.get('department')
        Gender=request.POST.get('Gender')
        Forms.objects.create(name=name,number=number,dob=dob,mobile=mobile,email=email,department=department,Gender=Gender,password=password,city=city,father=father,address=address)
    return render(request,'forms.html')
def signin(request):
    return render(request,'signin.html')
def signup(request):
    return render(request,'signup.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def result(request):
    result=Forms.objects.all()
    return render(request,'result.html',{"result":result})
def edit(request):
    edit=Forms.objects.all()
    return render(request,'edit.html',{"edit":edit})
