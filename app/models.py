from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=100)
    deptloc=models.CharField(max_length=100)

    def __str__(self):
        return self.deptname


class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    empname=models.CharField(max_length=100)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.empname

