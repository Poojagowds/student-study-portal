from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, DailyActivity, Attendance, Homework

# HOME
def home(request):
    notes = Note.objects.all()
    activities = DailyActivity.objects.all()
    attendance = Attendance.objects.all()
    homework = Homework.objects.all()

    return render(request, 'portal/home.html', {
        'notes': notes,
        'activities': activities,
        'attendance': attendance,
        'homework': homework
    })

# ADD NOTE
def add_note(request):
    if request.method == 'POST':
        Note.objects.create(
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('/')
    return render(request, 'portal/add_note.html')

# ADD ACTIVITY
def add_activity(request):
    if request.method == 'POST':
        DailyActivity.objects.create(
            activity_name=request.POST['activity_name'],
            date=request.POST['date']
        )
        return redirect('/')
    return render(request, 'portal/add_activity.html')

# ADD ATTENDANCE
def add_attendance(request):
    if request.method == 'POST':
        Attendance.objects.create(
            date=request.POST['date'],
            status=request.POST['status']
        )
        return redirect('/')
    return render(request, 'portal/add_attendance.html')

# ADD HOMEWORK
def add_homework(request):
    if request.method == 'POST':
        Homework.objects.create(
            subject=request.POST['subject'],
            description=request.POST['description'],
            due_date=request.POST['due_date']
        )
        return redirect('/')
    return render(request, 'portal/add_homework.html')

# EDIT NOTE
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)

    if request.method == 'POST':
        note.title = request.POST['title']
        note.content = request.POST['content']
        note.save()
        return redirect('/')

    return render(request, 'portal/edit_note.html', {'note': note})

# DELETE NOTE
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect('/')

# DELETE ACTIVITY
def delete_activity(request, activity_id):
    activity = get_object_or_404(DailyActivity, id=activity_id)
    activity.delete()
    return redirect('/')

# DELETE HOMEWORK
def delete_homework(request, homework_id):
    homework = get_object_or_404(Homework, id=homework_id)
    homework.delete()
    return redirect('/')
