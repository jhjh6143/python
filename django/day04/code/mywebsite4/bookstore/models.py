from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(verbose_name='书名',
                           max_length=50,
                           default='',
                           unique=True)
    pub=models.CharField('出版社',max_length=100,default='')
    price=models.DecimalField('定价',max_digits=7,
                              decimal_places=2,
                              default=0)
    market_price=models.DecimalField('零售价',max_digits=7,
                                     decimal_places=2,
                                     default=9999)
    def __str__(self):
        return "id:%d,书名：%s 出版社：%s"%(self.id,self.title,self.pub)

class Author(models.Model):
    name=models.CharField(verbose_name='姓名',
                          max_length=20,
                          unique=True,
                          db_index=True)
    age=models.IntegerField('年龄',
                            default=1)
    email=models.EmailField('邮箱',
                            null=True)
