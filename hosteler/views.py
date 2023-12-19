
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from hosteler.forms import CustomUserForm, StudentForm, RegistrationForm, ParentForm, FoodForm, NotiFications
from hosteler.models import User_Student, User_Parent, weekly_Food, notification


def new(request):
    return render(request, 'index.html')

def base(request):
    return render(request, 'admin.html')

def student(request):
    return render(request, 'student.html')

def parent(request):
    return render(request, 'parent.html')



def login_view(request):
    return render(request, 'login.html')


def stud_register(request):
    stud_form = StudentForm()
    reg_form = RegistrationForm()



    if request.method == 'POST':
        stud_form = StudentForm(request.POST, request.FILES)
        reg_form = RegistrationForm(request.POST)
        if stud_form.is_valid() and reg_form.is_valid():
            reg1 =reg_form.save(commit=False)
            reg1.is_student = True
            reg1.save()
            stud1 = stud_form.save(commit=False)
            stud1.user = reg1
            stud1.save()
            return redirect('login1')
        # Render the form with errors if it's not valid

    return render(request, "register.html", {"reg_form": reg_form, "stud_form": stud_form})

def parent_register(request):
    parent_form = ParentForm()
    reg_form = RegistrationForm()



    if request.method == 'POST':
        parent_form = ParentForm(request.POST, request.FILES)
        reg_form = RegistrationForm(request.POST)
        if parent_form.is_valid() and reg_form.is_valid():
            reg1 =reg_form.save(commit=False)
            reg1.is_parent = True
            reg1.save()
            parent1 = parent_form.save(commit=False)
            parent1.user = reg1
            parent1.save()
        # Render the form with errors if it's not valid

    return render(request, "register2.html", {"reg_form": reg_form, "parent_form": parent_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') #username is same as in the login.html page
        print(username)
        password = request.POST.get('pass') #pass is same in the login.html page
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('base') #base is the path name redirect to admin page
            elif user.is_student:
                return redirect('student') #student is the path name redirect to admin page
            elif user.is_parent:
                return redirect('parent') #parent is the path name redirect to admin page
        else:
            messages.info(request, 'Invalid Credentials')
    return render(request, 'login.html')

def view(request):
    data =  User_Student.objects.all()
    return render(request, "view_studentlist.html", {"data": data})

def view1(request):
    data =  User_Parent.objects.all()
    return render(request, "view_parentlist.html", {"data": data})


def delete(request,id):
    if request.method == 'POST':

        delt1 = User_Student.objects.get(id=id)
        reg_details= delt1.user
        delt1.delete()
        reg_details.delete()

        return redirect("view")
    return render(request,"admin.html")

def delete1(request,id):
    if request.method == 'POST':

        delt2 = User_Parent.objects.get(id=id)
        reg_details1= delt2.user
        delt2.delete()
        reg_details1.delete()

        return redirect("view1")
    return render(request,"admin.html")


def delete2(request,id):
    if request.method == 'POST':

        delt2 = notification.objects.get(id=id)

        delt2.delete()


        return redirect("view3")
    return render(request,"admin.html")



def update(request,id):
    stud_data = User_Student.objects.get(id=id)
    stud_reg_form = StudentForm(instance=stud_data)

    if request.method == 'POST':
        stud_reg_form1 = StudentForm(request.POST,request.FILES,instance=stud_data)
        if stud_reg_form1.is_valid():
            stud_reg_form1.save()
            return redirect("view")

    return render(request,'update.html',{'stud_form':stud_reg_form})

def food_register(request):
    food_form = FoodForm()



    if request.method == 'POST':
        food_form = FoodForm(request.POST, request.FILES)

        if food_form.is_valid():

            food1 = food_form.save(commit=False)
            food1.save()
            return redirect('view2')
        # Render the form with errors if it's not valid

    return render(request, "registerFood.html", { "food_form": food_form})


def view2(request):
    data =  weekly_Food.objects.all().order_by("id").values()
    return render(request, "view_foodlist.html", {"data": data})

def foodupdate(request,id):
    food_data = weekly_Food.objects.get(id=id)
    food_reg_form = FoodForm(instance=food_data)

    if request.method == 'POST':
        food_reg_form1 = FoodForm(request.POST,request.FILES,instance=food_data)
        if food_reg_form1.is_valid():
            food_reg_form1.save()
            return redirect("view2")

    return render(request,'food_update.html',{'food_form':food_reg_form})

def view_food_student(request):
    data = weekly_Food.objects.all()
    return render(request,"view_foodlist_student.html",{"data": data})

def ntf_register(request):
    ntf_form = NotiFications()




    if request.method == 'POST':
        ntf_form = NotiFications(request.POST, request.FILES)

        if ntf_form.is_valid():

            ntf1 = ntf_form.save(commit=False)
            ntf1.save()
            return redirect('view3')
        # Render the form with errors if it's not valid

    return render(request, "registerNotification.html", {"ntf_form": ntf_form})


def update_notification(request,id):
    ntf_data = notification.objects.get(id=id)
    ntf_reg_form = NotiFications(instance=ntf_data)

    if request.method == 'POST':
        ntf_reg_form1 = NotiFications(request.POST,request.FILES,instance=ntf_data)
        if ntf_reg_form1.is_valid():
            ntf_reg_form1.save()
            return redirect("view3")

    return render(request,'notification_update.html',{'ntf_form':ntf_reg_form})


def view3(request):
    data =  notification.objects.all().order_by("id").values()
    return render(request, "view_notification.html", {"data": data})

