from django.shortcuts import render
from .models import Exam


# Create your views here.
def index(request):
    exam = Exam.objects.all()
    return render(request, "index.html", {"exam": exam})
