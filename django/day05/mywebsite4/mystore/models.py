from django.db import models

# Create your models here.

class Publish(models.Model):
    name=models.CharField('出版社',max_length=100)
    def __str__(self):
        return "出版社"+self.name

class Author2(models.Model):
    name=models.CharField('作家2',max_length=50)
    def __str__(self):
        return '作家2'+self.name

class Book2(models.Model):
    title=models.CharField('书名2',max_length=50)
    pub_hose=models.ForeignKey(Publish,
                               on_delete=models.CASCADE,
                               null=True)
    authot=models.ManyToManyField(Author2,null=True)
    def __str__(self):
        return "书名2"+self.title


