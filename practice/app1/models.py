import time 
from django.db import models
from django.contrib.auth.models import User 


class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True , blank= True)
    Sname = models.CharField(max_length=30)
    username = models.CharField(max_length=20)
    mob = models.CharField(max_length=10)
    std = models.IntegerField(max_length=2)



class Fees(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True , blank= True)
    username = models.CharField(max_length=20)
    totalFees = models.IntegerField(null= True , blank= True,default=0)
    paidFees = models.IntegerField(null= True , blank= True,default=0)
    dueFees = models.IntegerField(null= True ,blank= True,default=0)


class Marks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True , blank= True)
    username = models.CharField(max_length=20)
    testDate = models.DateField(null= True , blank= True)
    subject = models.CharField(max_length=10,null= True , blank= True)
    totalMarks = models.IntegerField(max_length=10,null= True , blank= True)
    obtainedMarks = models.IntegerField(max_length=10,null= True , blank= True)



class StudentAttendence(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null= True , blank= True)
    username = models.CharField(max_length=20)
    date_01 = models.CharField(max_length=2,null= True , blank= True)
    date_02 = models.CharField(max_length=2,null= True , blank= True)
    date_03 = models.CharField(max_length=2,null= True , blank= True)
    date_04 = models.CharField(max_length=2,null= True , blank= True)
    date_05 = models.CharField(max_length=2,null= True , blank= True)
    date_06 = models.CharField(max_length=2,null= True , blank= True)
    date_07 = models.CharField(max_length=2,null= True , blank= True)
    date_08 = models.CharField(max_length=2,null= True , blank= True)
    date_09 = models.CharField(max_length=2,null= True , blank= True)
    date_10 = models.CharField(max_length=2,null= True , blank= True)
    date_11 = models.CharField(max_length=2,null= True , blank= True)
    date_12 = models.CharField(max_length=2,null= True , blank= True)
    date_13 = models.CharField(max_length=2,null= True , blank= True)
    date_14 = models.CharField(max_length=2,null= True , blank= True)
    date_15 = models.CharField(max_length=2,null= True , blank= True)
    date_16 = models.CharField(max_length=2,null= True , blank= True)
    date_17 = models.CharField(max_length=2,null= True , blank= True)
    date_18 = models.CharField(max_length=2,null= True , blank= True)
    date_19 = models.CharField(max_length=2,null= True , blank= True)
    date_20 = models.CharField(max_length=2,null= True , blank= True)
    date_21 = models.CharField(max_length=2,null= True , blank= True)
    date_22 = models.CharField(max_length=2,null= True , blank= True)
    date_23 = models.CharField(max_length=2,null= True , blank= True)
    date_24 = models.CharField(max_length=2,null= True , blank= True)
    date_25 = models.CharField(max_length=2,null= True , blank= True)
    date_26 = models.CharField(max_length=2,null= True , blank= True)
    date_27 = models.CharField(max_length=2,null= True , blank= True)
    date_28 = models.CharField(max_length=2,null= True , blank= True)
    date_29 = models.CharField(max_length=2,null= True , blank= True)
    date_30 = models.CharField(max_length=2,null= True , blank= True)
    date_31 = models.CharField(max_length=2,null= True , blank= True)

class Events(models.Model):
    image = models.ImageField(upload_to='')  
    year = models.IntegerField(max_length=4,null=True,blank=True)
    description = models.CharField(max_length=200)

class notes(models.Model):
    std = models.IntegerField(max_length=3,null=True,blank=True)
    subject = models.CharField(max_length=20,null = True, blank= True)
    chaptername = models.CharField(max_length=20,null = True, blank= True)
    notesFile = models.FileField(upload_to='pdfs/')
    


class NewAttandance(StudentAttendence):
    print()