from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.mail import send_mail

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError("User must enter email address")
        if not password:
            raise ValueError("users must have a password")

        user_obj = self.model(email =self.normalize_email(email))
        user_obj.set_password(password)
        # user_obj.admin = is_admin
        #user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    # def create_staffuser(self, email, password=None):
    #     user = self.create_user(email,password=password)
    #     user.staff = True
    #     user.save(using=self._db)
    #
    #     return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email,password=password)

        user.is_admin=True
        user.is_active=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, blank=True,null=True)
    last_name = models.CharField(max_length=255, blank=True,null=True)
    department = models.CharField(max_length=255, blank=True,null=True)
    faculty = models.CharField(max_length=255, blank=True,null=True)
    WHO_ARE_YOU_CHOICES =[
        ('STUDENT', "STUDENT"),
        ('LECTURER', "LECTURER"),
     ]
    who_are_you = models.CharField(max_length=8, choices=WHO_ARE_YOU_CHOICES, blank=True)
    def is_upperclass(self):
        return self.who_are_you


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()


    def email_user(subject,recipients, message, from_email):
        send_mail(
            subject,
            message,
            from_email,
            [recipients],
            fail_silently = False,

        )




    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


    @property
    def is_staff(self):
        return self.is_admin

    # @property
    # def is_admin(self):
    #     return self.admin
    # #
    # @property
    # def is_active(self):
    #     return self.is_active

# class Profile(models.Model):
#     WHO_ARE_YOU_CHOICES =[
#         ('STUDENT', "STUDENT"),
#         ('LECTURER', "LECTURER"),
#      ]
#     who_are_you = models.CharField(max_length=8, choices=WHO_ARE_YOU_CHOICES, default='LECTURER')
#
#     def is_upperclass(self):
#         return self.who_are_you
#     user = models.OneToOneField(User, on_delete = models.CASCADE)
#
#     first_name = models.CharField(max_length=255, blank=True,null=True)
#     last_name = models.CharField(max_length=255, blank=True,null=True)
#     department = models.CharField(max_length=255, blank=True,null=True)
#     faculty = models.CharField(max_length=255, blank=True,null=True)
#     # reg_number = models.CharField(max_length=12, blank=True,null=True)
#     # student = models.BooleanField(default=False)
