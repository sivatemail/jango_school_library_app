from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Books,BookStatus,user_books
from django.contrib.auth import login,logout,authenticate
from .forms import BookStatus_model_form
from django.contrib.auth.models import User

from django.contrib.auth.models import Permission,Group
from .models import Books


def user_login(request):
    if request.method=='POST':
        user = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user, password=password)
        if user is not None:
            login(request, user)

            if request.user.groups.filter(name='librarians').exists():
                return redirect('l_home')
            else:
                return redirect('s_home')

            return redirect('home')
        else:
            message = 'invalid credentials'
            return render(request, 'login.html', {'msg':message})
    else:
        return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')



def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'register.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})


def index(request):
    books = Books.objects.all()
    return render(request, 'home.html', {'data': books})


def student_home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if 'renew' in request.POST:
                book_id = request.POST['book_id']
                if BookStatus.objects.filter(book__book_id__exact=book_id, taken_by__exact=request.user):
                    bk = BookStatus.objects.get(book__book_id__exact=book_id, taken_by__exact=request.user)
                    bk.renewal_status = True
                    bk.save()
                    return redirect('s_home')
            else:
                pass
        else:
            books = BookStatus.objects.filter(taken_by=request.user)
            return render(request, 'student_home.html', {'books': books})

    else:
        if request.user.groups.filter(name='librarians').exists():
            print('hi')
        return redirect('login')


def librarian_home(request):
    if request.method=='POST':
        user = User.objects.get(id=request.POST['taken_by'])
        user_books.objects.get_or_create(user=user)
        count = user_books.objects.get(user=user)
        if count.books_count < 11:
            form = BookStatus_model_form(request.POST)
            form.save()
            count.books_count+=1
            count.save()
            book = Books.objects.get(book_id=request.POST['book'])
            book.available_quantity -= 1
            book.save()
            message = 'book has been alloted..'
            form = BookStatus_model_form()
            return render(request, 'staff_home.html', {'message':message, 'form': form})
        else:
            return redirect('l_home')



    else:
        form = BookStatus_model_form()
        return render(request, 'staff_home.html', {'form': form})










