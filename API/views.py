from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer
import requests
from bs4 import BeautifulSoup
import json
# Create your views here.

def index(request):
    return HttpResponse("Success")

class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

def latest(request):
    try:
        res  = requests.get('https://islamqa.info/en/latest')
        soup = BeautifulSoup(res.text, "html.parser")
        questions = soup.select(".post-card")
        for q in questions:
            url = q.attrs['href']
            content = q.select(".card-title")[0].getText()
            footer = q.select(".card-footer-item")[1]
            views = footer.select(".font-number")[0].getText()

            question  = Question()
            question.question = content
            question.link = url
            question.views = views

            question.save()
        return HttpResponse("Latest Data Fetched from Islamic QA")
    except e as Exception:
        return HttpResponse(f"Failed {e}")


        