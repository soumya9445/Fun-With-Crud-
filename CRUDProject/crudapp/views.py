from unicodedata import name
from django.shortcuts import render,redirect
from crudapp.models import StudentModel
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'crudapp/image.html')

def create(request):
    return render(request,'crudapp/create.html')   

def save(request):
    idno=request.POST.get('t1')
    na=request.POST.get('t2')
    con=request.POST.get('t3')
    em=request.POST.get('t4')
    fee=request.POST.get('t5')
    pas=request.POST.get('t6')
    img=request.FILES['t7']
    StudentModel(id=idno,name=na,contact=con,fees=fee,emailid=em,password=pas,photo=img).save()
    messages.success(request,'Employee Details Are Saved Successfully!!')
    return redirect('create')

def read(request):
    result=StudentModel.objects.all()
    return render(request,'crudapp/read.html',{"data":result})   

def update(request):
    idn=request.GET.get('sid')
    result=StudentModel.objects.get(id=idn)
    return render(request,'crudapp/update.html',{'data':result})   

def update_record(request):
    no=request.POST.get('t1')
    na=request.POST.get('t2')
    con=request.POST.get('t3')
    em=request.POST.get('t4')
    fee=request.POST.get('t5')
    pas=request.POST.get('t6')
    img=request.FILES['t7']
    StudentModel.objects.filter(id=no).update(name=na,contact=con,emailid=em,fees=fee,password=pas,photo=img)
    return redirect('read')

def delete(request):
    no=request.GET.get('sid')
    StudentModel.objects.filter(id=no).delete()
    return redirect('read')
        

def single_record(request):
    return render(request,'crudapp/single.html')

def search_one(request):
    idno=request.POST.get('s1')
    try:
        result=StudentModel.objects.get(id=idno)
        return render(request,'crudapp/single_record.html',{"data":result})

    except StudentModel.DoesNotExist:
        return render(request,'crudapp/single.html',{"error":'Invalid Idno'})    

def login(request):
    return render(request,'crudapp/login.html')        

def student_login(request):
    user=request.POST.get('s1')
    pas=request.POST.get('s2')
    try:
        StudentModel.objects.get(name=user,password=pas)
        messages.success(request,'login successfully!!')
        return redirect('read')    

    except StudentModel.DoesNotExist:
        #messages.error(request,'Invalid User')
        return render(request,'crudapp/login.html',{"error":'invalid user'}) 