from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


# the models for the user and the user object

class UserManager(BaseUserManager):
    def create_user(self, name, nickname, sex, profile, password=None ,admin = False, active=True, staff=False):
        if not name:
            raise ValueError('the user must have naem')
        if not nickname:
            raise ValueError('the user must have nickname')
        if not sex:
            raise ValueError('the user must have sex')
        
        user_obj = self.model(
            nick_name = nickname
        )
        user_obj.set_password(password)
        user_obj.name = name
        user_obj.sex = sex
        user_obj.profile = profile
        user_obj.admin = admin
        user_obj.active = active
        user_obj.staff = staff
        user_obj.save(
            using=self._db
        )
        return user_obj
    
    def create_superuser(self, name, nick_name, sex, password):
        user = self.create_user(
            name = name,
            nickname = nick_name,
            password=password,
            sex = sex,
            profile = 1,
            admin=True,
            active=True,
            staff=True
        )
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=100)
    nick_name = models.CharField(max_length=100, unique=True)
    sex = models.BooleanField()
    profile = models.IntegerField(verbose_name='Profile id')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='last login')
    admin = models.BooleanField(default=False)
    active = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'nick_name'


    REQUIRED_FIELDS = [
        'name',
        'sex',
    ]

    object = UserManager()

    def __str__(self):
        return self.nick_name

    def get_username(self):
        return self.nick_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active




# the models for the saved games.... 

class SavedGames(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    level = models.CharField(max_length=10, default='easy')
    mines_array = models.CharField(max_length=400, verbose_name='mines array') # holds the mines array
    opened_array = models.CharField(max_length=400,verbose_name='opened array') # holds the opened buttons array
    time = models.IntegerField()
        