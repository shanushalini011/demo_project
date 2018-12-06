from django.db import models
import datetime
from django import forms
from django.forms import ModelForm
class User(models.Model):

	active = models.BooleanField(default=False)
	fullname = models.CharField(max_length=2000)
	email = models.CharField(max_length =200, unique=True)
	mobile = models.BigIntegerField(default =True, unique=True)
	address = models.TextField(editable = False)
	dob = models.CharField(max_length = 100 , default = '')
	image = models.ImageField(upload_to='register/',default='default_pic.png')
	password = models.CharField(max_length =200, default ='')
	country =models.CharField(max_length =100,default = '')
	state =models.CharField(max_length = 100, default ='')
	city = models.CharField(max_length = 100 , default = '')
	gender=models.CharField(max_length=200, editable = False)
	api_key = models.TextField(editable = False)
	session_id=models.CharField(max_length=2000,default ='')
	added_date = models.DateTimeField(auto_now_add=datetime.datetime.now())
	updated_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.fullname+" - "+str(self.email)+"-"+str(self.id)