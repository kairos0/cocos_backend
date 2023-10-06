from django.db import models
from account.models import User
from product.models import Product

class BOARDTYPE(object):
    PRODUCT = 0
    QNA = 1

class Board(models.Model):
    title = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(auto_now_add=True)
    boardType = models.IntegerField(default=BOARDTYPE.QNA)
    description = models.TextField()
    views = models.IntegerField(default=0)

class Commnet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    commnet = models.TextField()
    # reply = models.ForeignKey('self', on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
