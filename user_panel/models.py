from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255,null=False)
	last_name = models.CharField( null=False , max_length=100)
	email = models.CharField( null=False , max_length=500)
	mobile = models.CharField( null=False,max_length=10 )
	image = models.FileField(default='user.png')
	position = models.CharField( null=False , max_length=500)
	email = models.CharField( null=False , max_length=500)
	school = models.CharField(null=True,blank=True,max_length=200,default="Enter Your Schooling")
	college = models.CharField(null=True,blank=True,max_length=200,default="Enter Your College Name")
	job = models.CharField(null=True,blank=True,max_length=200,default="Enter Your job place")
	position = models.CharField(null=True,blank=True,max_length=200,default="Enter Your Work position")

	def __str__(self):
		return self.first_name

class Post(models.Model):
	user = models.ForeignKey(Customer,on_delete=models.CASCADE)
	text = models.CharField(max_length=1000,null=False)
	image = models.FileField(null=True,blank=True)
	date = models.DateTimeField(auto_now_add = True,null=True)
	likes = models.IntegerField(default=0)
	dislikes = models.IntegerField(default=0)
	

	def __str__(self):
		return self.text
class Like(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	likes = models.IntegerField(default=0)
	user = models.ForeignKey(Customer,on_delete=models.CASCADE,default=0)
	dislikes = models.IntegerField(default=0)

class Comments(models.Model):
	user = models.ForeignKey(Customer,on_delete=models.CASCADE)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	review = models.CharField(max_length=1000,null=False)
	date = models.DateTimeField(auto_now_add = True,null=True)
	def __str__(self):
		return self.review
