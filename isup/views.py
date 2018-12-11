from django.shortcuts import render
from .models import Foundation

# Create your views here.
def home(request):
	return render(request, 'isup/home.html')

def disclaimer(request):
	return render(request, 'isup/disclaimer.html')

def whatisiota(request):
	return render(request, 'isup/whatisiota.html')

def wallets(request):
	return render(request, 'isup/wallets.html')

def tutorials(request):
	return render(request, 'isup/tutorials.html')

def foundation(request):
	foundation_roster = Foundation.objects.all()
	return render(request, 'isup/foundation.html', {'foundation': foundation_roster})

def buyiota(request):
	return render(request, 'isup/buyiota.html')