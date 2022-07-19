from django.shortcuts import render
from  django.http import HttpResponse
from .models import Maintenace
# Create your views here.

def index(request):
	dests = Maintenace.objects.all()
	
	return render(request, 'index.html', { 'dests': dests })

	# dest1 = Maintenace()
	# dest1.img = 's-1.jpg'
	# dest1.name = 'Tab Service Repairing'
	# dest1.desc = 'Repaire Tab'
	# dest1.price = 700
	# dest1.offer = True

	# dest2 = Maintenace()
	# dest2.img = 's-2.jpg'
	# dest2.name = 'Pipe Water Repairing'
	# dest2.desc = 'Repaire all your ducts pipe'
	# dest2.price = 650
	# dest2.offer = False


	# dest3 = Maintenace()
	# dest3.img = 's-3.jpg'
	# dest3.name = 'Washing machine Repairing'
	# dest3.desc = 'Repaire all types of machinery'
	# dest3.price = 780
	# dest3.offer = True

	# dest4 = Maintenace()
	# dest4.img = 's-4.jpg' 
	# dest4.name = 'Hand Washing Cleaning'
	# dest4.desc = 'Clean every type of house'
	# dest4.price = 980
	# dest4.offer = False

	# dests = [dest1, dest2, dest3, dest4]
