from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import template
from index.models import PttArticle,ArticleImage
from bs4 import BeautifulSoup
import requests
import re

# Create your views here.


def get_index(request):
    return render(request, 'index.html')


def show(request):
    url = request.POST["url"]
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    post = []
    article_detail = soup.find_all(class_ = "article-meta-value")
    #文章標題
    article_title = article_detail[2].text
    #日期處理
    article_datetime =  article_detail[3].text.split(' ')
    year = article_datetime[4]
    month = article_datetime[1]
    day = article_datetime[2]
    time = article_datetime[3]
    #月份轉換
    def month_transfer(str):
        switcher = {
            "Jan": "01","Feb": "02","Mar": "03","Apr": "04","May": "05","Jun": "06",
            "Jul": "07","Aug": "08","Sep": "09","Oct": "10","Nov": "11","Dec": "12",
        }
        return switcher.get(str, "0")
    #日期重組格式
    article_datetime =  year+"-"+month_transfer(month)+"-"+day+" "+time
    img_urls = soup.find(id='main-content').find_all('a')
    print(article_title)
    print(article_datetime)
    i = PttArticle.objects.create(ArticleTitle=article_title, ArticleDate=article_datetime)
    i
    for img_url in img_urls:
        if (img_url['href'].startswith('h') and img_url['href'].find("imgur")!=-1):
            ArticleImage.objects.create(ImageTitle = i, ImageURL = img_url['href'])
            post.append(img_url['href'])
            print(article_title+","+img_url['href'])
    
    return render(request,'show.html',locals()) 

def gallery(request):
    objs = PttArticle.objects.all()
    #objs2 = ArticleImage.objects.all()
    #print(objs)
    
    for obj in objs:
        print(obj)
        for url in obj.articleimage_set.all():
            print(url.ImageURL)
            #print(obj.articleimage_set.all())
    
    '''
    for obj in objs2:
        print(obj.ImageURL)
     '''   
    
    return render(request,'gallery.html',locals())

def delete(request):
    ArticleImage.objects.all().delete()
    PttArticle.objects.all().delete()
    return HttpResponseRedirect('/index/')