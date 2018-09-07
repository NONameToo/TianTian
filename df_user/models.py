# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=30)
    ureceive = models.CharField(max_length=20, default='')
    uaddr = models.CharField(max_length=100, default='')
    upostcode = models.CharField(max_length=6, default='')
    uphone = models.CharField(max_length=11, default='')
    class Meta:
        db_table = 'UserInfo'






