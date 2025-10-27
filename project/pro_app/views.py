from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Employee
from .serlizer import Empserlizer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def valid_file(pic):
    max=5*1024*1024
    if(pic.size>max):
        return False ,"size is too large"
    allow_type=['image/png','image/jpeg']
    if(pic.content_type not in allow_type):
        return False,"invalid type! type should in png,jpeg"
    return True,'valid response'
@csrf_exempt
def create_data(req):
    id=req.POST.get('id')
    name=req.POST.get('name')
    mail=req.POST.get('mail')
    pic=req.FILES['pic']

    isfile,msg=valid_file(pic)
    if(isfile):
        Employee.objects.create(emp_id=id,emp_name=name,emp_mail=mail,emp_pic=pic)
        Employee.save()
        return HttpResponse('msg')
    else:
        return HttpResponse(msg)
    


def read_user(req):
    data=Employee.objects.all()
    emp_data=Empserlizer(data,many=True)
    return JsonResponse({"data":emp_data.data})

@csrf_exempt
def update_user(req,id):
    try:
        single_data=Employee.objects.get(emp_id=id)
        user_data=json.loads(req.body)
        empser=Empserlizer(single_data,data=user_data,partial=True)
        if(empser.is_valid()):
            empser.save()
            return HttpResponse("user updated!")
    except:
        return HttpResponse("invalid")
@csrf_exempt
def delete_user(req,id):
    try:
        data=Employee.objects.get(emp_id=id)
        data.delete()
        return HttpResponse("deleted!")
    except:
        return HttpResponse("invalid ")



    





    
