from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from stdimage.models import StdImageField
from django.db import models


#カテゴリ機能の実装
class Category(models.Model):
    name = models.CharField('Category', max_length=50)
    def __str__(self):
        return self.name


#投稿機能の実装
class Create(models.Model):
    key = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category,verbose_name='Category',on_delete=models.PROTECT)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blog'


#自己紹介ページ機能
class About(models.Model):
    key = models.IntegerField()
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.CharField(max_length=20)
    product = models.CharField(max_length=100)
    skill = models.CharField(max_length=20)
    
    def __str__(self):
        return self.product


#homeの内容
class Home(models.Model):
    home_title = models.CharField(max_length=100)
    home_author = models.ForeignKey(User,on_delete=models.CASCADE)
    home_content = models.TextField()
    home_create_time = models.DateTimeField(default=timezone.now)
    home_category = models.ForeignKey(Category,verbose_name='Category',on_delete=models.PROTECT)

    def __str__(self):
        return self.home_title


#portfolio
class Portfolio(models.Model):
    project_name = models.CharField(max_length=200)
    image = StdImageField(upload_to='', blank=True, variations={
        'large': (540, 500,True),
        'thumbnail': (270, 250, True),
        'medium': (270, 500,True),
    })

    def __str__(self):
        return self.project_name


#Myart
class Myart(models.Model):
    project_name = models.CharField(max_length=200)
    image = StdImageField(upload_to='myarts/', blank=True, variations={
        'thumbnail': (270, 250, True),
    })

    def __str__(self):
        return self.project_name


#logoart
class Logoart(models.Model):
    project_name = models.CharField(max_length=200)
    image = StdImageField(upload_to='logoarts/', blank=True, variations={
        'thumbnail': (270, 250, True),
    })

    def __str__(self):
        return self.project_name


#videoart
class Videoart(models.Model):
    project_name = models.CharField(max_length=200)
    image = StdImageField(upload_to='videoarts/', blank=True, variations={
        'large': (540, 500,True),
    })

    def __str__(self):
        return self.project_name


#webdesign
class Webdesign(models.Model):
    project_name = models.CharField(max_length=200)
    image = StdImageField(upload_to='designs/', blank=True, variations={
        'large': (540, 500,True),
    })

    def __str__(self):
        return self.project_name


#フォームの内容
class Contact(models.Model):
    custmer_name = models.CharField(max_length=50)
    custmer_email = models.CharField(max_length=50)
    custmer_phonenumber = models.CharField(max_length=20)
    custmer_content = models.TextField()

    def __str__(self):
        return self.custmer_name


#参照機能の実装
class Read(models.Model):
    pass
#更新機能の実装
class Update(models.Model):
    pass
#削除機能の実装
class Delete(models.Model):
    pass
#タグ機能
class Tag(models.Model):
    pass
#スキルセット
class SkillSet(models.Model):
    pass
