from django.shortcuts import render
from onlinequiz.models import Exam

# Create your views here.
def examonline(request):
    results = Exam.objects.all()
    return render(request,"Index.html",{"Exam":results})