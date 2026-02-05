from email.mime import message
from django.shortcuts import redirect, render
from .models import Category, Item,ContactMessage,Achievement
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
# Create your views here.
def home(request):
     return render(request, 'home.html')

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    items = Item.objects.filter(category=category)
    return render(request, 'Content.html', {
        'category': category,
        'items': items
    })

def achievements(request):
    achievements_list = Achievement.objects.all().order_by('-created_at')

    return render(request, 'achievements.html', {
        'achievements': achievements_list
    })

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect("success")

    return render(request, "home.html")