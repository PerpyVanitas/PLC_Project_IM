from django.shortcuts import render,redirect
from .models import Department,Admin,Class,Mentee,Faculty,Calendar,Course,Attendance,Timetable,Mentor
from django.contrib import messages
from django.contrib.auth import logout


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')
