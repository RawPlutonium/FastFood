# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Customer(models.Model):
	"""docstring for Serve"""
	name =  models.CharField(max_length=100)
	clocation = models.CharField(max_length=100)
class restaurant(models.Model):
	"""docstring for restaurant"""
	name = models.CharField(max_length=100)
	rlocation = models.CharField(max_length=100)
class Food(models.Model):
	"""docstring for Food"""
	title = models.CharField(max_length=100)
	restaurant = models.ForeignKey(restaurant,on_delete=models.CASCADE)
	category = models.CharField(max_length=100)



		