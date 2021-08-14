from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    categoryname = models.CharField(_('category name'),max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.categoryname

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(_('title'),max_length = 100)
    slug = models.SlugField(_('slug'),unique=True)
    body = RichTextField(_('body'))
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(_('image'),default='default.jpg',blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)
    release_status = models.BooleanField(_('release status'),default=True)
    
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + ' ...'
