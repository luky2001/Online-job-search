from django.shortcuts import render
from django.http import HttpResponse
def home(request):
	people=[
 	  {'name':"Rohit",'age':14,'vill':"Maniyaripur"},
 	  {'name':"Sarvesh",'age':25,'vill':"Maniyaripur"},
 	  {'name':"Lallu",'age':43,'vill':"Maniyaripur"},
 	  {'name':"Deepak",'age':33,'vill':"Maniyaripur"},
 	  {'name':"Rahul",'age':27,'vill':"Maniyaripur"},
 	  {'name':"Paul",'age':15,'vill':"Maniyaripur"},
 	  {'name':"Vikash",'age':28,'vill':"Maniyaripur"},
 	  {'name':"Lakshmi",'age':21,'vill':"Maniyaripur"},
 	  {'name':"Nandani",'age':43,'vill':"Maniyaripur"},
 	  {'name':"Jyoti",'age':13,'vill':"Maniyaripur"}
	]
	return render(request,"home.html",context={'people':people})

def about(request):
	return render(request,"about.html")
def customer(request)

