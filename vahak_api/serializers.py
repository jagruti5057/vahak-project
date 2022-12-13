from rest_framework import serializers
from .models import Businesscard,Vehicalmodel,Attachnewlorry,phoneModel


# class usermodelserializer(serializers.ModelSerializer):
#     class Meta:
#         model  = UserModel
#         fields = '__all__'


class Businesscardserializer(serializers.ModelSerializer):
    class Meta:
        model  = Businesscard
        fields = '__all__'


class Vehicalmodelserializer(serializers.ModelSerializer):
    class Meta:
        model  = Vehicalmodel
        fields = '__all__'



class Attachnewlorryserializer(serializers.ModelSerializer):
    class Meta:
        model  = Attachnewlorry
        fields = '__all__'


class getPhoneNumberRegisteredserializer(serializers.ModelSerializer):
    class Meta:
        model  =phoneModel
        fields = '__all__'