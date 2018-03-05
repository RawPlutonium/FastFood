# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def landing(request):
	return render(request,'serve/landing.html')
def about(request):
	return render(request,'serve/about.html')
