from django.urls import path

from hosteler import views
#
# urlpatterns = [
#    path('new',views.new,name='new'),
#    path('base',views.base,name='base'),
#    path('login',views.login,name='login'),
#    path('register',views.registerPage,name='register')
#
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.new, name='new'),
    path('base/', views.base, name='base'),
    path('student/', views.student, name='student'),
    path('parent/', views.parent, name='parent'),
    path('login1', views.login_view, name='login1'),
    path('register/', views.stud_register, name='register'),
    path('register2/', views.parent_register, name='register2'),
    path('view/',views.view, name='view'),
    path('view1/',views.view1, name='view1'),
    path('delt/<int:id>/', views.delete, name='delt'),
    path('delts/<int:id>/', views.delete1, name='delts'),
    path('deltse/<int:id>/', views.delete2, name='deltse'),
    path('update1/<int:id>/', views.update, name='update1'),
    path('register3',views.food_register, name='register3'),
    path('view2',views.view2, name='view2'),
    path('update2/<int:id>/', views.foodupdate, name='update2'),
    path('stdfood', views.view_food_student, name='stdfood'),
    path('ntfreg', views.ntf_register, name='ntfreg'),
    path('update3/<int:id>/', views.update_notification, name='update3'),
    path('view3', views.view3, name='view3'),
    path('view4', views.view4, name='view4'),
    path('view5', views.view5, name='view5'),
    path('feedback', views.giveFeedback, name='feedback'),
    path('update4/<int:id>/', views.replytoFeedback, name='update4'),
    path('view6', views.view6, name='view6'),
    path('rooms', views.add_room, name='rooms'),
    path('view7',views.view_vacancy, name='view7'),
    path('vacancy', views.create_vacancy, name='vacancy'),
    path('delvacancy/<int:id>/',views.del_vacancy, name='delvacancy'),
    path('view8', views.view_book, name='view8'),
    path('appoint/<int:id>/', views.take_appointment, name='appoint'),
    path('cancel/<int:id>/', views.cancel_appointment, name='cancel'),
    path('view9', views.appointments, name='view9'),

]



# <!DOCTYPE html>
# <html lang="en">
# {% load crispy_forms_filters %}
# <head>
#     <meta charset="UTF-8">
#     <title>Title</title>
# </head>
# <body>
#     <h3>Register</h3>
#     <form method="POST" action="">
#         {% csrf_token %}
#         {{stud_form|crispy}}
#         {{reg_form|crispy}}
#         <input type="submit" name="Create User">
#
#     </form>
# </body>
# </html>

