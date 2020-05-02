from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

# Create your views here.
import json
from webapp.models import picM

#<<<<<<<<<<<<<<<<<<<<<<<<default route>>>>>>>>>>>>>>>>#
def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


#<<<<<<<<<<<<<<<<<<<<<<<<GET PIC Details >>>>>>>>>>>>>>>>#
def get_pic(request, pic_id):
    if request.method == 'GET':
        try:
            picOb = picM.objects.get(idd=pic_id)
            response = json.dumps([{ 'idd': picOb.idd,'name':picOb.name,'pic':picOb.pic}])
            
        except:
            response = json.dumps([{ 'Error': 'No Id with that name'}])
    return HttpResponse(response, content_type='text/json')

#<<<<<<<<<<<<<<<<<<<<<<<<POst PIC Details >>>>>>>>>>>>>>>>#
@api_view(['POST'])
def addId(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        picName=payload['name']
        picid=payload['idd']
        picUrl=payload['pic']
        
        picOb = picM(idd=picid,name=picName,pic=picUrl)
        try:
            picOb.save()
            response = json.dumps([{ 'Success': 'pic added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'pic could not be added!'}])
    return HttpResponse(response, content_type='text/json')