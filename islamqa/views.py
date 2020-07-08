from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

data = []

res  = requests.get('https://islamqa.info/en/latest')
soup = BeautifulSoup(res.text, "html.parser")
questions = soup.select(".post-card")
for q in questions:
    url = q.attrs['href']
    content = q.select(".card-title")[0].getText()
    footer = q.select(".card-footer-item")[1]
    views = footer.select(".font-number")[0].getText()
    data.append([content,url,views])


def index(request):
    return render(request, 'index.html', {'data':data})