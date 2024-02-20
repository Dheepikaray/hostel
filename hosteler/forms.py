

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from hosteler.models import User_Student, User_Parent, Register, weekly_Food, notification, feedback, rooms, vacancy, \
    Appointment

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

class feedbacks(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ('subject',)

class replyfeedback(forms.ModelForm):

    class Meta:
        model = feedback
        fields = ('subject','reply',)


class RoomCreationForm(forms.ModelForm):

    class Meta:
        model = rooms
        fields = ('no', 'student1', 'student2', 'student3')

class VacancyForm(forms.ModelForm):
    ch_slot = (('1','1'),('2','2'),('3','3'))
    slot = forms.ChoiceField(choices=ch_slot,widget=forms.RadioSelect)

    class Meta:
        model = vacancy
        fields = ('no','slot','vacant',)



from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['user', 'schedule', 'status']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #
    # STATUS_CHOICES = (
    #     (0, 'Pending'),
    #     (1, 'Confirmed'),
    #     (2, 'Cancelled'),
    # )
    #
    # status = forms.ChoiceField(choices=STATUS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    #
    #
