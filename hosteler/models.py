from django.contrib.auth.models import AbstractUser, User
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import BooleanField
from django.utils import timezone


# Create your models here.


#
class Register(AbstractUser):
    is_parent = BooleanField(default=False)
    is_student = BooleanField(default=False)




class User_Student(models.Model):
    user = models.ForeignKey('Register',on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    reg_no = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    email = models.EmailField()
    photo = models.FileField(upload_to='Pictures')

    def __str__(self):
        return f'{self.reg_no} {self.name}'


class User_Parent(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    reg_no = models.ForeignKey('User_Student', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    relation = models.CharField(max_length=100)
    # reg_no = models.CharField(max_length=100)
    student_name = models.CharField(max_length=100)
      # department = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^[6-9]\d{9}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=10, blank=True)
    email = models.EmailField()

class weekly_Food(models.Model):
    day = models.CharField(max_length=100)
    breakfast = models.CharField(max_length=100)
    lunch = models.CharField(max_length=100)
    dinner = models.CharField(max_length=100)

class notification(models.Model):
    date1 = models.DateTimeField(default=timezone.now)
    descriptions = models.CharField(max_length=100)

class feedback(models.Model):
    user = models.ForeignKey('Register', on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    subject = models.TextField(max_length=100)
    reply = models.TextField(null=True,blank=True)


class rooms(models.Model):
    no = models.CharField(max_length=4)
    student1 = models.ForeignKey('User_Student', on_delete=models.DO_NOTHING,related_name='student1')
    student2 = models.ForeignKey('User_Student', on_delete=models.DO_NOTHING,related_name='student2')
    student3 = models.ForeignKey('User_Student', on_delete=models.DO_NOTHING,related_name='student3')

    def __str__(self):
        return f'{self.no}'


class vacancy(models.Model):
    no = models.ForeignKey('rooms',on_delete=models.DO_NOTHING)
    slot = models.IntegerField(default=0)
    vacant = models.BooleanField(default=True)

class Appointment(models.Model):
    user = models.ForeignKey(User_Student, on_delete=models.CASCADE)
    schedule = models.ForeignKey(vacancy, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)











