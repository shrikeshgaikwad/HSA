from django.shortcuts import render,redirect,get_object_or_404 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from app1.models import * 
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from app1.models import *
from .forms import *
from . import settings
import os
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home (request):
    return render (request, "index.html")



def signup (request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        Sname = data.get('name')
        mob = data.get('mob')
        password = data.get('password')
        std = data.get('std')
        user = User.objects.create(
            username = username,
            first_name= Sname,
            mob = mob,         
        )
        user.set_password(password)
        user.save()

        student = Students.objects.create(
            user= user,
            Sname = Sname,
            username= username,
            std = std,
            mob = mob,
        )

        messages.info(request,'Account Created successfully')
        fees = Fees.objects.create(
            user=user,
            username = username,         
        )

        attendance = StudentAttendence.objects.create(
            user=user,
            username = username,         
        )

        marks = Marks.objects.create(
            user = user, 
            username = username,
        )


        return redirect ('/signup/')
    return render (request,"signup.html")



def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get('username')
        password = request.POST.get('password')
        if not (User.objects.filter(username=username).exists()):
            messages.error(request,'INVALID USERNAME')
            return redirect ('/login/')

        user = authenticate(username = username,password = password)
        if user is None :
            messages.error(request,'INVALID PASSWORD')
            print(user)
            return redirect ('/login/')
        else:
            login(request,user)
            return redirect ('/studentProfile/')
    return render (request, "login.html")









@login_required
def studentProfile (request):
    if request.user.is_superuser:
        fees = Fees.objects.all()
        attendance = StudentAttendence.objects.all()
        marks = Marks.objects.all()
        standard = request.POST.get('std')
        if standard in (str(0), None):  
            profile = Students.objects.all().order_by('-std')
            # student = auth_user.objects.all()

        else:
            standard = int(standard)
            profile = Students.objects.filter(std=standard)


        return render (request, "adminpage.html",{'profile':profile,'fees':fees,'attendance':attendance,'marks':marks,'standard':standard})

    else:
        profile = Students.objects.filter(user=request.user)
        fees = Fees.objects.filter(user=request.user)
        return render (request, "studentProfile.html",{'profile':profile,'fees':fees})


def logout_view(request):
    logout(request)  # Logs out the user
    return redirect('login')




@login_required
def manageEvent(request):
    if request.user.is_superuser:
        return render(request,"addEvent.html")


@login_required
def manage_notes(request):
    if request.method == "POST":
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('manage_notes')
    else:
        note = notes.objects.all().order_by('-std')
        urls = [note.url for note in note]
        form = NotesForm()

        return render(request, "manageNotes.html", {"form": form,"notes":note,"urls":urls})

@login_required
def delete_notes(request, notes_id):
    note = get_object_or_404(notes, id=notes_id)
    
    if notes.notesFile:
        file_path = os.path.join(settings.MEDIA_ROOT, str(notes.notesFile))

        print(f"File Path: {file_path}")
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print("File deleted successfully.")
            except Exception as e:
                print(f"Error deleting file: {e}")
    
    note.delete()  
    return redirect('/manage_notes/')  




@login_required
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_event')  # Redirect after upload
    else:
        events = Events.objects.all().order_by('-year')

        form = EventForm()
        return render(request, "addEvent.html", {"form": form,"events":events})



@login_required
def delete_event(request, event_id):
    events = get_object_or_404(Events, id=event_id)
    
    # Delete image file from media folder
    if events.image:
        image_path = os.path.join(settings.MEDIA_ROOT, str(events.image))
        if os.path.exists(image_path):
            os.remove(image_path)
            events.delete()
            return redirect('/addEvent/') 









def event_gallery(request):
    events = Events.objects.all().order_by('-year')
    return render(request, 'events.html', {'events': events})


@login_required
def update_marks(request):
    if request.method == "POST":
        changes = json.loads(request.POST.get("changes"))  # Parse JSON data

        try:
            for change in changes:
                mark = Marks.objects.get(username=change["id"])
                setattr(mark, change["field"], change["value"])
                mark.save()

            return JsonResponse({"status": "success"})

        except Marks.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Record not found"})

    return JsonResponse({"status": "error", "message": "Invalid request"})







@csrf_exempt
def updateDatabase(request):

    if request.method == "POST" :
        data = json.loads(request.body)
        updated_data = data.get('data', [])
        print(updated_data)

        for row in updated_data:

            username = row.get('column_0')
            name = row.get('column_1')
            newstd = row.get('column_2')
            mobile = row.get('column_3')
            fees = row.get('column_4')
            due = row.get('column_5')
            try:
                student = Students.objects.get(username=username)
                
                #student.Sname = name
                student.std = newstd
                student.mob = mobile
                student.totalFees = fees
                student.dueFees = due
                student.save()
            except Students.DoesNotExist:
                print(f"Student with username '{username}' not found.")




        return JsonResponse({'success': True})


@login_required
def attendance(request):
    if request.user.is_superuser:
        attendance = StudentAttendence.objects.all()
        standard = request.POST.get('std')
        if standard in (str(0), None):  
            profile = Students.objects.all().order_by('-std')
        else:
            standard = int(standard)
            profile = Students.objects.filter(std=standard)
        return render (request, "adminattandance.html",{'profile':profile,'attendance':attendance})
