from django.shortcuts import render
from django.http import HttpResponse

def submit(request):
    return HttpResponse("Exam submitted successfully")

def show_exam_result(request):
    return HttpResponse("Displaying exam result")
