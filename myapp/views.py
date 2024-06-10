from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import book
from django.contrib.auth import authenticate,login,logout




def home(request):
    return render(request, 'home.html')


def admin_booklist(request):
    books = book.objects.all()
    return render( request, "main.html", {'books':books})

def signdetail(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        fname=request.POST.get('firstname')
        lname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')    
        if password1!=password2:
            messages.info(request,"Password are not same!....")
            return redirect('/signin')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists....")
                return redirect('/signin')
            user=User.objects.create_user(username=username,first_name=fname, last_name=lname, email=email,password=password1)
            user.save()
            return redirect ('/')

        
    return render(request, 'signin.html')


def logindetail(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')

        if not User.objects.filter(email = email).exists():
            messages.info(request,"You entered wrong credential Check again....")
            return redirect('/')            
        user = User.objects.get(email = email)
        un=user.username
        user=authenticate(username=un,password=password)
        
        if user is not None:
            if user.is_staff ==True:
                login(request,user)
                return redirect('/admin-booklist/')
            else:
                login(request,user)                
                return redirect('/user/booklist/')
        else:
            return redirect('/')
         
    # return render(request,'main.html')



def addbook(request):
    if request.method=="POST":
        name=request.POST.get('name')
        author=request.POST.get('author')
        pages=request.POST.get('pages')
        price=request.POST.get('price')

        b=book.objects.create(name=name, author=author, pages=pages, price=price)
        b.save()
        b_list=book.objects.all()
        messages.info(request, "Book is added to list")
        return redirect('/admin-booklist/') 
    return render(request, 'addbook.html')
    

def deletebook(request,id):
    b=book.objects.get(id=id)
    b.delete()
    messages.info(request, "Book delete Successfully")
    return redirect("admin-booklist")


def edit(request, id=None):
    if request.method=='POST':
        b=book.objects.get(id=id)
        b.name = request.POST.get('name')
        b.author = request.POST.get('author')
        b.pages = request.POST.get('pages')
        b.price = request.POST.get('price')
        b.save()
        return redirect('/admin-booklist/')
    
    bookd = book.objects.get(id=id)
    return render(request, 'edit.html', {'id':id, "book":bookd})   

def user_booklist(request):
    books=book.objects.all()
    return render(request, "user.html", {'books':books})

def logout_user(request):
    logout(request)
    return redirect('/')
