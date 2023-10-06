from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import User, AdminType, RegisterStatus, UserLoginLogs
from django.db.models import Q
from django.contrib import auth
from datetime import datetime
from ..serializers import UserSerializer

class RegisterChecker(APIView):
    # url patten : /register/status/?userid=[userid]&email=[email]
    # Check for duplicates of userid or email
    def get(self, request):
        userID=request.GET.get("userid")
        email=request.GET.get("email")

        status = User.objects.filter(Q(username=userID)|
                                     Q(email=email))
        if len(status) > 0 :
            return Response(RegisterStatus.ERROR)
        else:
            return Response(RegisterStatus.OK)

class Register(APIView):
    def post(self, request):
        data = request.data

        user = User.objects.create_user(email=data["email"],
                                   realName=data["realName"],
                                   birthday=data["birthday"])
        user.set_password(data["password"])
        user.save()

        userlogin = auth.authenticate(email=data["email"], password=data["password"])
        if userlogin:
            print("login pass")
        else:
            print("fail")
        return Response(RegisterStatus.OK)

class SignUp(APIView):
    def post(self, request):
        data = request.data
        print(request.user, request.session)
        userlogin = auth.authenticate(email=data["email"], password=data["password"])

        if userlogin:
            auth.login(request, userlogin)
            print(request.user, request.session)
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')

            signUpLogs = UserLoginLogs.objects.create(user=userlogin, ipAddress=ip)
            signUpLogs.save()
            return Response(RegisterStatus.OK)
        else:
            print("login fail")
            return Response(RegisterStatus.ERROR)

class Logout(APIView):
    def get(self, request):
        auth.logout(request)
        return Response(RegisterStatus.OK)