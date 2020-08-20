from rest_framework import serializers
from django.conf import settings
from .models import Hotel

MAX_NAME_LEN=240
HOTEL_ACTION_OPTIONS=settings.HOTEL_ACTION_OPTIONS


class HotelActionSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    action=serializers.CharField()
    def validate_action(self, val):
        val=val.lower().strip()
        if val not in HOTEL_ACTION_OPTIONS:
            raise serializers.ValidationError('NOT A VALID ACTION')
        return val

class hotel_action_serializer(serializers.Serializer):
    action          =serializers.CharField()
    name            =serializers.CharField()
    price           =serializers.CharField()
    link            =serializers.CharField()
    def validate_action(self, val):
        val=val.lower().strip()
        if val not in HOTEL_ACTION_OPTIONS:
            raise serializers.ValidationError('NOT A VALID ACTION')
        return val

class HotelSerializer(serializers.ModelSerializer):
    likes=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Hotel
        fields=['id','name','price','link','likes']

    def get_likes(self,obj):
        return obj.saved_by.count()

    def validate_name(self, value):
        if len(value)>MAX_NAME_LEN:
            raise serializers.ValidationError('NAME TOO LONG')
        return value
