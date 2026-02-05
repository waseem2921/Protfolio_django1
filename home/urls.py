from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<slug:slug>/', views.category_detail, name='category_detail'),
    path('contact/', views.contact, name='contact'),
    path('achievements/', views.achievements, name='achievements'),

]

