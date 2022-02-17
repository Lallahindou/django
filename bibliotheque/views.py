from importlib.metadata import files
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import BookForm, CategoryForm
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from  .decorators import admin_only, unauthenticated_user, allowed_users, admin_only

#from .models import tbl_Authentification
#from .forms import SignupForm


@unauthenticated_user    
def registerPage(request):
   
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():

            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='lecteur')
            user.groups.add(group)
            messages.success(request,'Acount was created for' +username)
            return redirect('login')

         
    context = {'form':form}
    return render(request,'accounts/register.html', context)

#@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Username OR password is incorrect') 
                    #return render(request,'accounts/login.html')   

    context = {}
    return render(request,'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def userPage(request):
    context = {}
    return render(request, 'accounts/user.html',context)


@login_required(login_url='login')
@admin_only
def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save() 

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save() 



    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailble': Book.objects.filter(status='availble').count(),

    }
    return render(request,'pages/index.html',context) 

@login_required(login_url='login')
@allowed_users(allowed_roles=['lecteur'])
def index_ut(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save() 

        add_category = CategoryForm(request.POST)
        if add_category.is_valid():
            add_category.save() 



    context = {
        'category': Category.objects.all(),
        'books': Book.objects.all(),
        'form': BookForm(),
        'formcat': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'booksold': Book.objects.filter(status='sold').count(),
        'bookrental': Book.objects.filter(status='rental').count(),
        'bookavailble': Book.objects.filter(status='availble').count(),

    }
    return render(request,'pages/index_ut.html',context) 


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def books(request):
    search = Book.objects.all()

    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)




    context = {
        'category': Category.objects.all(),
        'books': search,
        'formcat': CategoryForm(),
    }
    return render(request,'pages/books.html',context) 


@login_required(login_url='login')    
#@allowed_users(allowed_roles=['lecteur'])
def books_ut(request):
    search = Book.objects.all()

    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)




    context = {
        'category': Category.objects.all(),
        'books_ut': search,
        'formcat': CategoryForm(),
    }
    return render(request,'pages/Books_ut.html',context)  


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)   
    context = {
        'form':book_save,
    } 
    return render(request, 'pages/update.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html') 






    