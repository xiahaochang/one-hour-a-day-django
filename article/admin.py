'''
Description: 
Date: 2021-08-13 16:36:11
LastEditTime: 2021-08-13 16:55:09
LastEditors: xiahaochang
'''
from django.contrib import admin

# Register your models here.
# 别忘了导入ArticlerPost
from .models import ArticlePost

# 注册ArticlePost到admin中
admin.site.register(ArticlePost)
