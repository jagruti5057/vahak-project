from django.shortcuts import render
from .models import Businesscard,Vehicalmodel,Attachnewlorry
from rest_framework.views import APIView
from .serializers import Businesscardserializer,Vehicalmodelserializer,Attachnewlorryserializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import phoneModel
import base64
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
import optparse


# # Create your views here.

def index(request): 
    return render(request,'index.html')


# class UserAPI(APIView):
#     def get(self,reuest,format=None):
#         user = User.objects.all()
#         serializer = userserializer(user,many=True)
#         return Response(serializer.data,status=200)


# class UserAPI(APIView):
#     def get(self,reuest,format=None):
#         user = User.objects.all()
#         serializer = userserializer(user,many=True)
#         return Response(serializer.data,status=200)


#     def post(self,request,format=None):
#         serializer = userserializer(data=request.data)
#         if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#         return Response(serializer.errors)

    
#     def put(self, request, id, format = None):
#         user = User.objects.get(id=id)
#         serializer = userserializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)

#     def delete(self,request,id,format=None):
#         user = User.objects.get(id=id) 
#         user.delete()
#         return Response()
     

class BusinesscardAPI(APIView):
    def get(self,reuest,format=None):
        user = Businesscard.objects.all()
        serializer = Businesscardserializer(user,many=True)
        return Response(serializer.data,status=200)



    def post(self,request,format=None):
        serializer = Businesscardserializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BusinessCardUpdateAPI(APIView):     
    def put(self, request, id, format = None):
        user = Businesscard.objects.get(id=id)
        serializer = Businesscardserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self,request,id,format=None):
        user = Businesscard.objects.get(id=id) 
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class VehicalmodelAPI(APIView):
    def get(self,reuest,format=None):
        user = Vehicalmodel.objects.all()
        serializer = Vehicalmodelserializer(user,many=True)
        return Response(serializer.data,status=200)



    def post(self,request,format=None):
        serializer = Vehicalmodelserializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)



class VehicalmodelUpdateAPI(APIView):
        
    def put(self, request, id, format = None):
        user = Vehicalmodel.objects.get(id=id)
        serializer = Vehicalmodelserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def delete(self,request,id,format=None):
        user = Vehicalmodel.objects.get(id=id) 
        user.delete()
        return Response()



class AttachnewlorryAPI(APIView):
    def get(self,reuest,format=None):
        user = Attachnewlorry.objects.all()
        serializer = Attachnewlorryserializer(user,many=True)
        return Response(serializer.data,status=200)



    def post(self,request,format=None):
        serializer = Attachnewlorryserializer(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors)

class AttachlorryUpdateAPI(APIView):    
    def put(self, request, id, format = None):
        user = Attachnewlorry.objects.get(id=id)
        serializer = Attachnewlorryserializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    
    def delete(self,request,id,format=None):
        user = Attachnewlorry.objects.get(id=id) 
        user.delete()
        return Response()



        
class generateKey:
    @staticmethod
    def returnValue(phone):
        return str(phone) + str(datetime.date(datetime.now())) + "Some Random Secret Key"


class getPhoneNumberRegistered(APIView):
    # Get to Create a call for OTP
    @staticmethod
    def get(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)  # if Mobile already exists the take this else create New One
        except ObjectDoesNotExist:
            phoneModel.objects.create(
                Mobile=phone,
            )
            Mobile = phoneModel.objects.get(Mobile=phone)  # user Newly created Model
        Mobile.counter += 1  # Update Counter At every Call
        Mobile.save()  # Save the data
        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Key is generated
        OTP = optparse.HOTP(key)  # HOTP Model for OTP is created
        print(OTP.at(Mobile.counter))
        # Using Multi-Threading send the OTP Using Messaging Services like Twilio or Fast2sms
        return Response({"OTP": OTP.at(Mobile.counter)}, status=200)  # Just for demonstration
    def post(request, phone):
        try:
            Mobile = phoneModel.objects.get(Mobile=phone)
        except ObjectDoesNotExist:
            return Response("User does not exist", status=404)  # False Call

        keygen = generateKey()
        key = base64.b32encode(keygen.returnValue(phone).encode())  # Generating Key
        OTP = optparse.HOTP(key)  # HOTP Model
        if OTP.verify(request.data["otp"], Mobile.counter):  # Verifying the OTP
            Mobile.isVerified = True
            Mobile.save()
            return Response("You are authorised", status=200)
        return Response("OTP is wrong", status=400)

