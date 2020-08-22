from django.shortcuts import render
import json,sys,os
# Create your views here.

from django.conf import settings
from .serializers import HotelSerializer,hotel_action_serializer
from rest_framework.response import  Response
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import Hotel
ROOT_PATH=str(os.path.sep).join(str(settings.BASE_DIR).split(os.path.sep)[:-2])
if ROOT_PATH not in sys.path:sys.path.append(ROOT_PATH)
#print(sys.path)
from Scraping.HotelDomains import main as hd

ALLOWED_HOSTS=settings.ALLOWED_HOSTS


def welcome_view(request):
    context={}
    return render(request,'personal/welcome_page.html',context)


def home_search_view(request):
    return render(request,'personal/home_search.html')

@api_view(['GET','POST'])
def all_results_view(request,hotels=None,*args,**kwargs):
    context={}
    user=request.user
    if not user.is_authenticated:user=None
    if request.method=='POST':
        data=request.data
        query=data.get('query')
        '''
        Write the code for the search functionality
        '''

        hotels=hd(query)
        if user:
            already_saved = Hotel.objects.filter(saved_by=user)

        for (index,hotel) in enumerate(hotels,start=1):
            hotel['id']=index
            hotel['is_saved']=False
            if user and already_saved.filter(link=hotel['link']).exists():
                hotel['is_saved'] = True
        data=json.dumps(hotels)
        context['data']=data
        return render(request,'personal/resultPage.html',context=context)
    return Response(hotels)



@api_view(['POST',])
@authentication_classes([SessionAuthentication])
@permission_classes([IsAuthenticated])
def hotel_action_view(request,*args,**kwargs):
    user=request.user
    data=request.data
    serializer=hotel_action_serializer(data=data)
    if serializer.is_valid(raise_exception=True):
        data=serializer.validated_data
        action=data.get('action')
        obj,created=Hotel.objects.get_or_create(
            name=data.get('name'),
            price=data.get('price'),
            link=data.get('link')
        )

        if action=='save':
            obj.saved_by.add(user)
            serializer = HotelSerializer(obj)
            return Response(serializer.data, status=200)
        elif action=='unsave':
            try:
                obj.saved_by.remove(user)
            except Exception as e:
                return Response({'message':'You haven\'t even saved it yet.'})
        else:
            return Response({'message': 'Invalid action'})
    return Response({},status=200)
