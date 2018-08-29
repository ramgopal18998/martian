from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from . models import Customer,Post,Comments,Like
from django.core import serializers
#from bson import json_util

def logout_user(request):
	print("dasd");
	logout(request)
	return redirect('/login')

@csrf_exempt
def root(request):
	return redirect('/home')
def values(request):
	if request.method == "POST":
		val = request.POST.get('change')
		text = request.POST.get('text')
		print(val)
		print(text)
		customer = Customer.objects.get(user_id=request.user.id)
		if text == "school":
			customer.school = val
		if text == "college":
			customer.college = val
		if text == "job":
			customer.job = val
		if text == "position":
			customer.position = val;
		customer.save()
		print("saved")
		return HttpResponse("sucess")

@csrf_exempt
def status(request):
	if request.method == "POST":
		file = request.FILES.get('file')
		text = request.POST.get('status-text')
		print(file)
		post = Post()
		user = Customer.objects.get(user_id=request.user.id)
		post.image = file
		post.user = user
		post.text = text
		post.save()
		print("saved")
		
		return redirect('/home')


@csrf_exempt
def datafetch(request):
	if request.method == "POST":
		id = request.POST['id']
		print(id)
		a = int('0' + id)
		posts = Post.objects.all().order_by('-date')[a-1:a+3]
		print(posts)
		data = serializers.serialize('json', posts)
		return HttpResponse(data,'application/json')


@csrf_exempt
def new_comments(request):
	if(request.method == "POST"):
		id = request.POST.get('id')
		text = request.POST.get('text')
		name = request.POST.get('user')
		print(name)
		print(text)
		comments = Comments();
		customer = Customer.objects.get(first_name=name)
		post = Post.objects.get(id=id)
		comments.user = customer
		comments.post = post
		comments.review = text
		comments.save()
		return HttpResponse("success")

@csrf_exempt
def comments(request):
	print("/home/comment called")
	if request.method == "POST":
		id = request.POST['id']
		print(id)
		comments = Comments.objects.filter(post_id=id).order_by('date')
		
		#print(comments)
		i = 0
		#print(data)
		data = []
		for obj in comments:
			data.append({"name":obj.user.first_name,"review":obj.review,"link":obj.user.image.url,'time':str(obj.date)})

		
		#data = serializers.serialize('json', data )
		list_json = json.dumps(data)
		return HttpResponse(list_json,'application/json')




@csrf_exempt
def home(request):
	if request.method == "POST":
		id = request.POST.get('id')
		text = request.POST.get('val')

		customer = Customer.objects.get(user_id=request.user.id)
		#print(id)
		try:
			like = Like.objects.get(post_id=id,user=customer)
			return HttpResponse("error")
		except:
			like = Like()
			post = Post.objects.get(id=id)
			if text == 'like':
				post.likes = post.likes +1;
			else:
				post.dislikes = post.dislikes +1;
			post.save()
			like.post = post
			like.user = customer
			like.save()
			return HttpResponse("successful")

	if not request.user.is_authenticated():
		return redirect('/login')
	else:
		user = User.objects.get(id=request.user.id)
		customer = Customer.objects.get(user_id=user.id)
		posts = Post.objects.all().order_by('-date')
		return render(request,'index.html',{'customer':customer,'posts':posts})


	return render(request,'index.html')

@csrf_exempt
def login_user(request):
	if request.method == "GET":
		return render(request,'user_panel/login.html')
	else:
		email = request.POST['username']
		password = request.POST['password']
		user = User.objects.get(email=email)
		if user is None:
			return render(request, 'user_panel/login.html', {'error_message': 'Invalid login'})
		else:
			user = authenticate(username=user.username, password=password)
		if user is not None:
			if user.is_active:
				login(request,user)
				print(user)
				customer = Customer.objects.get(user_id=request.user.id)
				posts = Post.objects.all()
				print(customer)
				return redirect('/home')
			else:
				return render(request, 'user_panel/login.html', {'error_message': 'Your account has been disabled'})
		else:
			return render(request, 'user_panel/login.html', {'error_message': 'Invalid login'})
		

@csrf_exempt
def register(request):
	if(request.method == "GET"):
		return render(request,'user_panel/register.html')
	else:
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		email = request.POST['email']
		mobile = request.POST['mobile']
		password = request.POST['password']
		image = request.FILES.get('image',False)
		user = User()
		user.username = first_name
		user.set_password(password)
		user.email = email
		user.save()
		customer = Customer()
		customer.user = user
		customer.first_name = first_name
		customer.last_name  = last_name
		customer.mobile = mobile
		customer.email
		if image != False:
			customer.image = image
		customer.save()
		return redirect('/login')

