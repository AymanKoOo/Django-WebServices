from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import pyodbc
# Create your views here.
import json
from webapp.models import picM

#<<<<Connect SQL SERVER DB>>>>>>


def conection():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=DESKTOP-MPMVGIB\SQLEXPRESS;"
        "Database=NuzhaTec;"
        "Trusted_Connection=yes;"
        )
    return conn
    
#<<<<<<<<<<<<<<<<<<<<<<<<default route>>>>>>>>>>>>>>>>#
def index(request):
  
    conn=conection();
    cursor = conn.cursor()
    cursor.execute("select * from Nzha_ServicePhoto")
    for row in cursor:
        response = json.dumps(f'row = {row}')
        print(json.dumps(f'row = {row}'))
    conn.close()
    return HttpResponse(response, content_type='text/json')


#<<<<<<<<<<<<<<<<<<<<<<<<GET PIC Details >>>>>>>>>>>>>>>>#
def get_pic(request, pic_id):
    if request.method == 'GET':
        
             conn=conection();
             cursor = conn.cursor()
             cursor.execute("select * from Nzha_ServicePhoto where ID="+pic_id)
             for row in cursor:
               response = json.dumps(f'row = {row}')
               print(json.dumps(f'row = {row}'))
         
             conn.close()   
                  
    return HttpResponse(response, content_type='text/json')

#<<<<<<<<<<<<<<<<<<<<<<<<POst PIC Details >>>>>>>>>>>>>>>>#
@api_view(['POST'])
def addId(request):
    if request.method == 'POST':

            payload = json.loads(request.body)

            ID=payload['ID']
            photoFilePath=payload['photoFilePath']
            Nzha_Service_ID=payload['Nzha_Service_ID']
            Nzha_User_ID=payload['Nzha_User_ID']
            filterString=payload['filterString']

            conn = conection()
            cursor = conn.cursor()
            sql = """\
            EXEC SP_ServicePhoto @ID=?,@photoFilePath=?,@Nzha_Service_ID=?,@Nzha_User_ID=?,@filterString=?
            """
            params =  (ID, photoFilePath,Nzha_Service_ID,Nzha_User_ID,filterString)
            cursor.execute(sql, params)
            conn.commit()
            response = json.dumps(f'row = {"done"}')
            
    return HttpResponse(response, content_type='text/json')