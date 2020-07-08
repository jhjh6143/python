#file:mtwebsite_db/bookstore/models.py

from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField('书名',max_length=50)
    pub=models.CharField('出版社的名字',max_length=50,null=True)
