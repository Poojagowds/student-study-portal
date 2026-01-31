from django.contrib import admin
from .models import Note, DailyActivity, Attendance, Homework

admin.site.register(Note)
admin.site.register(DailyActivity)
admin.site.register(Attendance)
admin.site.register(Homework)
