# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def landing(request):
	return render(request,'serve/landing.html')
def about(request):
	return render(request,'serve/about.html')
def order(request):
	if request.method == 'GET':
		area = request.GET['area']
		place = request.GET['where']
		hse = request.GET['number']
	return render(request,'serve/order.html',{'area' : area, 'place' : place,'hse' : hse})
def signup(request):
	return render(request,'serve/signup.html')