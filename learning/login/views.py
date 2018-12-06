from django.shortcuts import render
from django.http import Http404,HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from django.utils import timezone
import os
from .models import User

import json
from django.conf import settings
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_protect
from django.template import loader
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
import hashlib
from random import randint
from django.views.generic import TemplateView
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate




@api_view(["POST", "GET"])
@parser_classes((JSONParser,))
def login(request):

    if request.method == "GET":
        
        if request.session.has_key('mykey'): 
            print ('logged in')

            # template = loader.get_template("admin_home.html")
             # company = get_object_or_404(Company)
            context = {} 
            response = redirect('/login/home')
            return response
            # return HttpResponse(template.render(context, request))
        else:
            template = loader.get_template("login.html")
            context = {}
        return HttpResponse(template.render(context, request))
    elif request.method=="POST" and request.session.has_key('mykey')==False:
        print("request data",request.data)
        try: 
            d=request.data
            # print("d=",d)
            email=d['email']
            # print("email",email)

            password=d['password']
            user = User.objects.get(email=email,password=password) 
            
            if user.active==False:
               request.session['mykey'] = 'myvalue'
               return Response({"active":user.active,"status":200,"message":"already deactived"}) 
            else:
                
                return Response({"active":user.active,"status": 200, "userId":user.id,"message": "successfully logged in " + user.fullname }, status=200)

        except Exception as e: 

            print("user",e)
            return Response({"status": 400, "message": "Email does not exist in our PMT account"}, status=400)
def logout(request):
    try: 
        # if request.session.has_key('mykey'):

            print('del')

            s_id = request.COOKIES['sessionid']
            del request.session['mykey']

            print('deleted')
            response = redirect('/login/')
            return response


    except:
        template = loader.get_template("login.html")   
        context = {}
        response = redirect('/login/')
        return response

def home(request):
  # session_key = request.COOKIES['sessionid']
  # print('id ',request.session.session_key,'\n',session_key)
  print ('you are awesome!')
  template = loader.get_template("home.html")


  
  
  # user_sessions = User.objects.filter(id = session_key)
  
  if request.session.has_key('mykey'):

      id = request.COOKIES['sessionid']
      print(request.COOKIES)
      template = loader.get_template("login.html")
      # user = User.objects.all()
      

      
      context = {}
  else:
      
      context = {}
  # company = get_object_or_404(Company)
  
  # return render(request, 'home.html',context)
  return HttpResponse(template.render(context, request))
