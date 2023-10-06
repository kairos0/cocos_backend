from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Product, ProductImage, ProductSlideImage
from ..serializers import ProductSlideImageSerializer
from account.models import User
import string
import random
import os
import json

class TempProductItem(APIView):
    def get(self, request):
        #tmp
        user = User.objects.get(email="cocos2@cocos.com")
        ###
        product = Product.objects.create(user=user, isTemp=True)

        return Response(product.id)

class ProductSlideImageUpload(APIView):
    def post(self, request):
        data = request.data
        slideIdx = data['slideIdx']
        changeImgName = data['imageFile']
        string_pool = string.ascii_letters + string.digits
        name, ext = os.path.splitext(changeImgName.name)
        randomStr = ""
        for i in range(10) :
            randomStr += random.choice(string_pool)
            
        target = Product.objects.get(id=data['productID'])

        changeImgName.name = randomStr + ext

        img = ProductSlideImage.objects.create(product = target,
                                               index = slideIdx,
                                               image = changeImgName,
                                               isMainImage = True if slideIdx == 0 else False)
        


        return Response(ProductSlideImageSerializer.data)

class ProductImageUpload(APIView):
    def post(self, request):
        data = request.data
        changeImgName = data['imageFile']
        string_pool = string.ascii_letters + string.digits
        name, ext = os.path.splitext(changeImgName.name)
        randomStr = "" 
        for i in range(10) :
            randomStr += random.choice(string_pool)
            
        target = Product.objects.get(id=data['productID'])

        changeImgName.name = randomStr + ext

        img = ProductImage.objects.create(product = target,
                                    image=changeImgName)
        
        return Response(img.image.url)