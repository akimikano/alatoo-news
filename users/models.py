from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class AccountManager(BaseUserManager):
    def create_user(self, student_id, name_surname, password=None):
        if not student_id:
            raise ValueError('Student ID must be set!')
        user = self.model(student_id=student_id, name_surname=name_surname, password=password)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, student_id, name_surname, password):
        user = self.create_user(student_id, name_surname, password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    student_id = models.CharField(max_length=9, unique=True)
    name_surname = models.CharField(max_length=40)

    USERNAME_FIELD = 'student_id'
    REQUIRED_FIELDS = ['name_surname']

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = AccountManager()

    def get_short_name(self):
        return self.student_id

    def get_full_name(self):
        return self.student_id

    def has_perm(self, perm, ob=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def natural_key(self):
        return self.student_id





