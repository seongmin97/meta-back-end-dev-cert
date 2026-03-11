from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Little Lemon!")

# def about(request):
#     return HttpResponse("About us")

# def menu(request):
#     return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")

def drinks(request, drink_name):
    drink_list = {
        'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment'
    }
    choice_of_drink = drink_list[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

from myapp.forms import BookingForm

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)

# def menu(request):
#     menu_item = Menu.objects.all()
#     item_dict = {"menu": menu_item}
#     return render(request, "menu.html", item_dict)

# def about(request):
#     about_content = {'about': "Little Lemon is a family-owned Mediterranean restaurant, focused on traditional recipes served with a modern twist. The chefs draw inspiration from Italian, Greek, and Turkish culture and have a menu of 12–15 items that they rotate seasonally. The restaurant has a rustic and relaxed atmosphere with moderate prices, making it a popular place for a meal any time of the day."} 
#     return render(request, "about.html", about_content)


# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')

def book(request):
    return render(request, 'book.html')