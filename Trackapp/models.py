from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Master(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    isactive = models.BooleanField(default=True, verbose_name="Active")
    created_user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ['-isactive']



class Course(models.Model):
      class_choices=(
            
            (u'Python','Python'),
            (u'Full Stack Developer','Full Stack Developer'),
            (u'Software Testing','Software Testing'),
            (u'Digital Marketing','Digital Marketing')
      )
class Student(models.Model):
    id = models.AutoField(primary_key=True) 
    Username_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student',default=None)
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    Address=models.CharField(max_length=200)
    ContactNumber=models.BigIntegerField()
    Trainer=models.ForeignKey('Teacher',on_delete=models.CASCADE)
    Course=models.CharField("Course",max_length=20, choices = Course.class_choices)
    Batch=models.CharField(max_length=10)
    
    def __str__(self):
        return self.FirstName

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher',default=None)
    FirstName=models.CharField(max_length=10)
    LastName=models.CharField(max_length=10)
    Course=models.CharField("Course",max_length=20, choices = Course.class_choices,default=None)
    def __str__(self):
        return self.FirstName
class Manager(models.Model):
     Username=models.ForeignKey(User,on_delete=models.CASCADE,related_name='Manager',default=None)
     FirstName=models.CharField(max_length=10)
     LastName=models.CharField(max_length=10)
     def __str__(self):
        return self.FirstName
class Attendence(models.Model):
      Student=models.ForeignKey('Student',on_delete=models.CASCADE,default=None)
      TotalNumberOfDays=models.BigIntegerField()
      NoOfDaysPresent=models.BigIntegerField()
      def __str__(self):
        return self.Student
class Mark(models.Model):
      Student=models.ForeignKey('Student',on_delete=models.CASCADE,default=None)
      MarksObtained=models.BigIntegerField()
      OutOf=models.BigIntegerField(default=None)
      def __str__(self):
        return self.Student
        


def __str__(self):
        return self.FirstName
    
class Meta:
        db_table='studentrecord'
       