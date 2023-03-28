from django.db import models
from django.utils.html import format_html

class Product(models.Model):
    title = models.CharField(max_length=250,null=False,blank=False)
    image = models.ImageField(upload_to = 'images/',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):  
    return self.title
@property
def picture(self):
    return format_html('<img src= "{}" width="50" height="50" style="border_radius:50% " />'.format(self.image.url) )


class InfoModel(models.Model):
    admin_telegram_username = models.CharField(max_length=60)
    admin_phone_number = models.TextField()
    bot_username = models.CharField(max_length=100,blank=True)

class UsersModel(models.Model):
    username = models.TextField(null=True, blank=True)
    telegram_id = models.CharField(max_length=20)
    lang = models.CharField(max_length=2,blank=True)
    def __str__(self):
        return self.username