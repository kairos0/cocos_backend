from django.urls import path
from ..views.views import TempProductItem, ProductImageUpload, ProductSlideImageUpload

urlpatterns = [
    path('newtemp/', TempProductItem.as_view()),
    path('image/upload/', ProductImageUpload.as_view()),
    path('slide/upload/', ProductSlideImageUpload.as_view())
]
