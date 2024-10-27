from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Book
from .forms import BookForm

# Create your views here.

def home(request):
    books = Book.objects.all()
    ctx = {"books": books}

    return render(request, "base.html", context=ctx)

def create_book(request):
    bookForm = BookForm()

    if request.method == "POST":
        bookForm = BookForm(request.POST)
        if bookForm.is_valid():
            bookForm.save()
            return redirect("home")
    return render(request, 'book_create.html', context={'form': bookForm})

def detail_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    return render(request, "detail_book.html", context={"book": book})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home')

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    bookform = BookForm(instance=book) # BookForm-ს instance-ად გადააწოდე შენი პოსტი და ფორმაში ველები უკვე შევსებული იქნება მონაცემებით
    if request.method == 'POST':
        bookform = BookForm(request.POST, instance=book) # BookForm-ს თუ instance-ად გადაცემ შენ ობიექს ახლის შექმნი მაგოვრად იმ შენს გადაცემულ ობიუექტს განაახლებს
        if bookform.is_valid(): # მონაცემების ვალიდურობის შემოწმება
            bookform.save() # ჩანაწერის ბაზაში შენახვა
            return redirect('home') 
    return render(request, 'update_book.html', context={'form': bookform})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('home')

