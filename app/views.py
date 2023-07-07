from django.shortcuts import render
from django.http import HttpResponse
from app.models import *


# Create your views here.
def dept(request):
    if request.method=='POST':
        num=request.POST['deptno']
        name=request.POST['deptn']
        loc=request.POST['deptloc']
        DO=Dept.objects.get_or_create(deptno=num,deptname=name,deptloc=loc)[0]
        DO.save()
        return HttpResponse('Data Submitted')
        
    return render(request,'dept.html')


def emp(request):
    EM=Dept.objects.all()
    d={'EM':EM}
    if request.method=='POST':
        enum=request.POST['eno']
        ename=request.POST['ename']
        num=request.POST.get('deptno')
        DO=Dept.objects.get(deptno=num)
        EO=Emp.objects.get_or_create(empno=enum,empname=ename,deptno=DO)[0]
        EO.save()
        return HttpResponse('Data is inserted')


    return render(request,'emptable.html',d)
