from django.shortcuts import render,redirect
# from django.http import HttpResponse
from AdminApp.models import Category,Product,UserInfo,PaymentMaster
from UserApp.models import MyCart
# Create your views here.
def homepage(request):
    cat=Category.objects.all()
    prod=Product.objects.all()
    return render(request,"homepage.html",{"cat":cat,"prod":prod})


def login(request):
    if(request.method=='GET'):
        return render(request,"login.html",{})
    else:
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        try:
            user=UserInfo.objects.get(username=uname, password=pwd)
        except:
            return redirect(login)
        else:
            request.session["username"]=uname
            return redirect(homepage)
        

def signout(request):
    request.session.clear()
    return redirect(homepage)


def signup(request):
    if(request.method=="GET"):
        return render(request,"signup.html",{})
    else:
        uname=request.POST['uname']
        email=request.POST['email']
        pwd=request.POST['pwd']
        s1=UserInfo()
        s1.username=uname
        s1.email=email
        s1.password=pwd
        s1.save()
        # return HttpResponse("Inserted successfully")

        return redirect(homepage)


def viewdetails(request,did):
    cat=Category.objects.all()
    prod=Product.objects.get(id=did)
    return render(request,"viewdetails.html",{"prod":prod,"cat":cat})


def showcakes(request,did):
    cat=Category.objects.all()
    id=Category.objects.get(id=did)
    prod=Product.objects.filter(cat=id)
    return render(request,"homepage.html",{"prod":prod,"cat":cat})


def cart(request):
    if(request.method =="POST"):
        if("username" in request.session):
            prodid=request.POST["prodid"]
            user=request.session["username"]
            qty=request.POST["qty"]
            user=UserInfo.objects.get(username=user)
            prod=Product.objects.get(id=prodid)
            try:
                cart=MyCart.objects.get(cakes=prod,users=user)
            except:
                
                cart=MyCart()
                cart.users=user
                cart.cakes=prod
                cart.qty=qty
                cart.save()
            else:
                pass    
            return redirect(homepage)
        else:
            return redirect(login)

def showallrecord(request):
    uname=request.session["username"]
    user=UserInfo.objects.get(username=uname)
    if(request.method == "GET"):
        cartitem=MyCart.objects.filter(users=user)
        total = 0

        for mon in cartitem:
            total += mon.qty * mon.cakes.price
        request.session["total"]=total
       
        return render(request,"cart.html",{"item":cartitem}) 
    else:
        id=request.POST["cakeid"]
        cake=Product.objects.get(id=id)
        item=MyCart.objects.get(users=user,cakes=cake)
        qty=request.POST["qty"]
        item.qty=qty
        item.save()
        return redirect (showallrecord)

def delete(request,did):
    if(request.method=='GET'):
        
            item=MyCart.objects.get(id=did) 
            item.delete() 
            
            return redirect(showallrecord)

def Makepayment(request):
    if(request.method == 'GET'):
         return render(request,"Makepayment.html")
    else:
        cardnumber=request.POST['cardnumber']  
        cvv=request.POST['cvv'] 
        expiry=request.POST['expiry'] 
        try:
            buyer=PaymentMaster.objects.get(cardnumber=cardnumber,cvv=cvv,expiry=expiry)
        except:
            return redirect(Makepayment)
        else:
            owner=PaymentMaster.objects.get(cardnumber='12345',cvv='789',expiry='1233') 
            owner.balance += request.session["total"]
            buyer.balance -= request.session["total"] 
            owner.save()
            buyer.save()
        return redirect(homepage)
        