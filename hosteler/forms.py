

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from hosteler.models import User_Student, User_Parent, Register, weekly_Food, notification

from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = Register
        fields = ('username','email','first_name','last_name',)

class DateInput(forms.DateInput):
    input_type='date'

class RegistrationForm(UserCreationForm):
    Username = forms.CharField()
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = Register
        fields = ('username','password1','password2')



class StudentForm(forms.ModelForm):
    dob=forms.DateField(widget=DateInput)
    print(dob)
    CH = (('M', 'Male'), ('F', 'Female'),('O','Other'))
    gender = forms.CharField(widget=forms.RadioSelect(choices=CH))
    ch = (('initial', '--------'),('CS', 'Computer Science'),('CE', 'Civil'),('EC', 'Electronics and Communication'),('EEE', 'Electrical and Electronics'),('ME', 'Mechanical'))
    department = forms.ChoiceField(choices=ch)
    class Meta:
        model = User_Student
        fields = ('name','dob','gender','address','reg_no','department','phone','email','photo',)




class ParentForm(forms.ModelForm):
    CH = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = forms.CharField(widget=forms.RadioSelect(choices=CH))
    class Meta:
        model = User_Parent
        fields = ('name','reg_no','gender','address','relation','student_name','phone','email',)


class FoodForm(forms.ModelForm):
    CH = (('Initial','Select day'),('Monday', 'Monday'),('Tuesday', 'Tuesday'),('Wednesday', 'Wednesday'),('Thursday', 'Thursday'),('Friday', 'Friday'),('Saturday', 'Saturday'),('Sunday', 'Sunday'))
    day = forms.ChoiceField(choices=CH)
    Ch = (('Initial','Select BreakFast'),('Poori & Tea/Coffee','Poori & Tea/Coffee'),('Dosa & Tea/Coffee','Dosa & Tea/Coffee'),('Idli & Tea/Coffee','Idli & Tea/Coffee'),('Bread Omlet & Tea/Coffee','Bread Omlet & Tea/Coffee'),('Masala Dosa & Tea/Coffee','Masala Dosa & Tea/Coffee'),('Chappati & Tea/Coffee','Chappati & Tea/Coffee'),('Puttu & Tea/Coffee','Puttu & Tea/Coffee'))
    breakfast = forms.ChoiceField(choices=Ch)
    Ch1 = (('Initial','Select Lunch'),('Meals','Meals'),('Vegetable Biriyani','Vegetable Biriyani'),('Chicken Biriyani','Chicken Biriyani'),('Fried Rice','Fried Rice'),('Meals with Chicken Curry','Meals with Chicken Curry'),('Meals with Fish Fry','Meals with Fish Fry'),('Ghee Rice','Ghee Rice'))
    lunch = forms.ChoiceField(choices=Ch1)
    Ch2 = (('Initial','Select Dinner'),('Appam & Egg Curry','Appam & Egg Curry'),('Chappathi & Chicken Curry','Chappathi & Chicken Curry'),('Meals','Meals'),('Chicken Biriyani','Chicken Biriyani'),('Vegetable Biriyani','Vegetable Biriyani'),('Fried Rice','Fried Rice'),('Porotta','Porotta'))
    dinner = forms.ChoiceField(choices=Ch2)
    class Meta:
        model = weekly_Food
        fields = ('day','breakfast','lunch','dinner')

class NotiFications(forms.ModelForm):
    date1 = forms.DateField(widget=DateInput)
    class Meta:
        model = notification
        fields = ('date1','descriptions')
