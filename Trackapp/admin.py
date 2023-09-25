from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Teacher,Student,Attendence,Mark,Manager
# Register your models here.
class MyUserAdmin(UserAdmin):
    
    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        super().save_model(request, obj, form, change)
        # if(change == False):
        if (obj.groups.filter(name="Teacher").exists() == True):
                print("Teacher")
                t = Teacher()
                t.FirstName = obj.first_name
                t.LastName = obj.last_name
                t.user = obj
                t.Course = "Python"
                t.save()
        
        if (obj.groups.filter(name="Student").exists() == True):
                print("Student")
                t = Student()
                t.FirstName = obj.first_name
                t.LastName = obj.last_name
                t.Username_id = obj
                t.Address = "xyz"
                t.ContactNumber = "123"
                t.Trainer = "sunitha"
                t.Course = "Python"
                t.Batch = "abc"
                t.save()


    


admin.site.unregister(User)
admin.site.register(User,MyUserAdmin)

class Studentadmin(admin.ModelAdmin):
    list_display=('id','FirstName','LastName')
    ordering=('FirstName',)
    search_fields=('FirstName',)

class Teacheradmin(admin.ModelAdmin):
    list_display=('id','FirstName','LastName')
    ordering=('FirstName',)
    search_fields=('FirstName',)
class Attendenceadmin(admin.ModelAdmin) :
    list_display=('id','TotalNumberOfDays','NoOfDaysPresent')
    ordering=('NoOfDaysPresent',)
class Markadmin(admin.ModelAdmin):
    list_display=('id','MarksObtained','OutOf') 
    ordering=('MarksObtained',) 
class Manageradmin(admin.ModelAdmin):
    list_display=('FirstName','LastName')
    ordering=('FirstName',)       


admin.site.register(Student,Studentadmin,)
admin.site.register(Teacher,Teacheradmin,)
admin.site.register(Attendence,Attendenceadmin,)
admin.site.register(Mark,Markadmin,)
admin.site.register(Manager,Manageradmin,)

