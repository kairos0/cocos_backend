from django.urls import path
from ..views.views import Register, RegisterChecker, SignUp, Logout

urlpatterns = [
    path('register/', Register.as_view()),
    path('register/status/', RegisterChecker.as_view()),
    path('signup/', SignUp.as_view()),
    path('logout/', Logout.as_view()),
]