from django.db import models
from account.models import UserLoginLogs, User

class Product(models.Model):
    name = models.TextField()
    price = models.IntegerField(default=0)
    uploadDate = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isTemp = models.BooleanField(null=False)
    # log = models.ForeignKey(UserLoginLogs, on_delete=models.CASCADE)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # log = models.ForeignKey(UserLoginLogs, on_delete=models.CASCADE)
    uploadDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to="image/", blank=True) # 이미지 컬럼 추가

class ProductSlideImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    index = models.IntegerField()
    uploadDate = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="image/")
    isMainImage = models.BooleanField()
