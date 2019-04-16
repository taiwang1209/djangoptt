from django.shortcuts import render
from django import template
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.
def get_index(request):
    return render(request,'index.html')

def show(request):
    a = "123"
    url = request.POST["url"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    post = []
    img_tag = soup.find(id='main-content').find_all('a')
    
    for img in img_tag:
        if (img['href'].startswith('h') and img['href'].find("imgur")!=-1 ):
            post.append(img['href'])
            print(img['href'])

    return render(request, 'show.html',locals())