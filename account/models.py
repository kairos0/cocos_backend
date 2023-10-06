from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class RegisterStatus(object):
    OK = 0
    ERROR = -1
    # if needed details
    #EXSIST_EMAIL = -1
    #EXSIST_USERID = -2

class AdminType(object):
    REGULAR_USER = "Regular User"
    ADMIN = "Admin"
    SUPER_ADMIN = "Super Admin"

class UserManager(BaseUserManager):
    def create_user(self, email, realName, birthday, password=None):
        if email is None:
            raise TypeError(_('Users should have a Email.'))

        user = self.model(email=self.normalize_email(email), realName=realName, birthday=birthday)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.TextField(unique=True)
    realName = models.TextField()
    birthday =  models.TextField()
    createTime = models.DateTimeField(auto_now_add=True)
    permission = models.TextField(default=AdminType.REGULAR_USER)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [email]

    objects = UserManager()

    def __str__(self):
        return self.email

class UserLoginLogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accessTime = models.DateTimeField(auto_now_add=True)
    ipAddress = models.TextField()