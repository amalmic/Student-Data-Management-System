
from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name='home'),
    path("display",views.display_teacher,name='display_teacher'),
    path("display1",views.display_student,name='display_student'),
    # path('marks',views.display_marks,name='display_student'),
    # path('accounts/login/',views.loginview,name='login'),
    # path('passwordreset',views.resetPassword,name='resetpassword'),
    # path('student-details/', views.student_details, name='student_details'),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    # path('studentnav/<str:fname>/',views.studentnav,name='studentnav')
]