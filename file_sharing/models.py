from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    first_name = None
    last_name = None
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=255)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.id)


class Group(models.Model):
    name = models.CharField(max_length=255)
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_groups')
    members = models.ManyToManyField(
        User, related_name='group_members')  # Updated related_name


class File(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=80, null=True, blank=True)
    file = models.FileField(upload_to='uploads/')
    uploaded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='uploaded_files')
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="files")  # Updated related_name
    is_private = models.BooleanField(default=False)
