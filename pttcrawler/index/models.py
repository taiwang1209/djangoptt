from django.db import models

# Create your models here.
class PttArticle(models.Model):
    ArticleTitle = models.CharField(max_length=100)
    ArticleDate = models.CharField(max_length=100)
    def __str__(self):
        return self.ArticleTitle

class ArticleImage(models.Model):
    ImageTitle = models.ForeignKey('PttArticle',on_delete=models.CASCADE,default='')
    ImageURL = models.URLField(max_length=100)
    def __str__(self):
        return self.ImageTitle.ArticleTitle
