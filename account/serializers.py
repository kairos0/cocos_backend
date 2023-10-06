from rest_framework import serializers
from .models import User, UserLoginLogs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class UserLoginLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLoginLogs
        fields = "__all__"