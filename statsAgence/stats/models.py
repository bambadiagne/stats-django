from django.db import models
import csv
import tempfile
import shutil
from statsAgence.settings import MEDIA_ROOT
from os import close, remove
import datetime

class Article(models.Model):
    nom = models.CharField(max_length=70)
    image = models.CharField(max_length=200)
    price=models.FloatField()
    quantite = models.IntegerField()
    type_categorie = models.CharField(max_length=200)
    description = models.TextField()
    date_creation =models.DateTimeField(auto_now_add=True)
    
    
class Product(models.Model):
    numero_transfert = models.CharField(max_length=70)
    price=models.FloatField()
    pin = models.CharField(max_length=4)
    caissier=models.CharField(max_length=70)
    agence=models.CharField(max_length=100)
    code_agence=models.CharField(max_length=10)
    agence_reconciliation=models.CharField(max_length=100)
    code_agence_reconciliation=models.CharField(max_length=10)
    montant_envoye=models.BigIntegerField()
    devise_envoi=models.CharField(max_length=10)
    pays_envoi=models.CharField(max_length=50)
    pays_destination=models.CharField(max_length=50)
    montant_a_payer=models.FloatField()
    devise_de_paiement=models.CharField(max_length=10)
    montant_commission=models.FloatField()
    devise_commission=models.CharField(max_length=10)
    date_creation =models.DateTimeField(auto_now_add=True)
    taux=models.FloatField(max_length=100)
    tob=models.BigIntegerField()
    tthu=models.BigIntegerField()
    frais = models.BigIntegerField()
    action=models.CharField(max_length=20)
   

def handle_uploaded_file(source):
    fd, filepath = tempfile.mkstemp(prefix=source.name, dir=MEDIA_ROOT)
    with open(filepath, 'wb') as dest:
        shutil.copyfileobj(source, dest)
    close(fd)    
    return filepath
def import_csv(filename,model_name):
    print(filename)
    with open(filename) as f:
        reader = csv.reader(f)
        first_line=0
        for model_object in reader:
                
            if(first_line==0):
                first_line+=1
            else:
                if(model_name=="article"):
                    new_article= Article(*tuple(model_object))
                    new_article.save()
                elif(model_name=="product"):
                    list_date=list(map(int,model_object[17].split(" ")[0].split('/')))
                    list_heure=list(map(int,model_object[17].split(" ")[1].split(':')))
                    model_object[17]=datetime.datetime(list_date[-1],list_date[0],list_date[1],list_heure[0],list_heure[1])
                    new_product= Product(*tuple(model_object))
                    new_product.save()

    remove(filename)