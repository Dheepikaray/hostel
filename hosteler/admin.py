from django.contrib import admin

# Register your models here.

from django.contrib import admin

from hosteler import models

admin.site.register(models.Register)
admin.site.register(models.User_Student)
admin.site.register(models.User_Parent)
admin.site.register(models.weekly_Food)
admin.site.register(models.notification)
admin.site.register(models.rooms)
admin.site.register(models.feedback)
