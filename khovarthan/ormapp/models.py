from django.db import models

from django.db import models
from django.contrib import admin
class items(models.Model):
    pname=models.CharField(max_length=100)
    pid=models.IntegerField(primary_key=True)
    ptype=models.CharField(max_length=100)
    pprice=models.IntegerField()
    warranty=models.CharField(max_length=10)
    return_or_replacement_policy=models.TextField()
    sellercontact=models.IntegerField()
    selleremail=models.EmailField()

class itemsAdmin(admin.ModelAdmin):
    list_display=["pname","pid","ptype","pprice","warranty","return_or_replacement_policy","sellercontact","selleremail"]
