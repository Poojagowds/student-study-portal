from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class DailyActivity(models.Model):
    activity_name = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.activity_name


class Attendance(models.Model):
    date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[('Present', 'Present'), ('Absent', 'Absent')]
    )

    def __str__(self):
        return f"{self.date} - {self.status}"


class Homework(models.Model):
    subject = models.CharField(max_length=50)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return self.subject
