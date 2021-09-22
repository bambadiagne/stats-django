from django.db import models
import csv

class Article(models.Model):
    nom = models.CharField(max_length=70)
    image = models.CharField(max_length=200)
    price=models.FloatField()
    quantite = models.IntegerField()
    type_categorie = models.CharField(max_length=200)
    description = models.TextField()
    date_creation =models.DateTimeField(auto_now_add=True)
    
    @staticmethod
    def import_csv(cls,filename):
        with open(filename) as f:
            reader = csv.reader(f)
            for article in reader:
                new_article= Article(article)
                new_article.save()