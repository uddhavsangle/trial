from django.shortcuts import render,HttpResponseRedirect
from .models import CurdModel
from.forms import CurdForms,UserForm
from django.contrib.auth.decorators import login_required

from .serializer import Apiser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
@login_required()
def form_view(r):
    if r.method=='POST':
        form=CurdForms(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data')
    return render(r,'form.html',{'form':CurdForms})
@login_required()
def show_data(r):
    return render(r,'show_data.html',{'data':CurdModel.objects.all})
@login_required()
def update(r,id):
    obj=CurdModel.objects.get(id=id)
    if r.method=="POST":
        form=CurdForms(r.POST,instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data')
    return render(r,'form.html',{'obj':obj})
@login_required()
def delete(r,id):
    obj = CurdModel.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/data')

def sign_up(r):
    if r.method == 'POST':
        form = UserForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/data')
    return render(r, 'signup.html', {'form': UserForm})

class myapi(APIView):
    def get(self,r):
        abc=CurdModel.objects.all()
        sr=Apiser(abc,many=True)
        return Response(sr.data)
    def post(self,r):
        srobj=Apiser(data=r.data)
        if srobj.is_valid():
            srobj.save()
            return Response(srobj.data,status=status.HTTP_201_CREATED)
        return Response(srobj.errors,status=status.HTTP_400_BAD_REQUEST)

class myapi2(APIView):
    def put(self,r,pk):
        obj=CurdModel.objects.get(pk=pk)
        srobj = Apiser(obj,data=r.data)
        if srobj.is_valid():
            srobj.save()
            return Response(srobj.data, status=status.HTTP_201_CREATED)
        return Response(srobj.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        obj = CurdModel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)








