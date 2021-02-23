from django.shortcuts import render
from Login_app.models import NewUser
from django.contrib import messages

# Create your views here.
def Indexpage(request):
    return render(request,'index.html')

def Userreg(request):
    if request.method=='POST':
        Username=request.POST['Username1']
        Email=request.POST['Email1']
        Pwd=request.POST['Pwd1']
        Gender=request.POST['Gender']
        NewUser(Username=Username,Email=Email,pwd=Pwd,Gender=Gender).save()
        messages.success(request,'The New User' +request.POST['Username1']+ "Is Saved Successfully...!")
        return render(request,'Registration.html')
    else:
        return render(request,'Registration.html')

def loginpage(request):
    if request.method=="POST":
        try:
            Userdetails=NewUser.objects.get(Username=request.POST['Email'],pwd=request.POST['Pwd'])
            print("Username=",Userdetails)
            request.session["Email"]=Userdetails.Email
            return render(request,'index.html')
        except NewUser.DoesNotExist as e:
            messages.success(request,'Username / Password Invalid..!')
    return render(request,'Login.html')

def logout(request):
    try:
        del request.session['Email']
    except:
        return render(request,'index.html')
    return render(request,'index.html')


