from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse

# Create your views here.
def home(request):
    form = StudentRegistration()
    stu = User.objects.all()
    return render(request, 'enroll/home.html', {'form':form, 'stu':stu})

def save_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            stuid = request.POST.get('sid')
            name = request.POST['name']     
            # name = form.cleaned_data['name']
            email = request.POST['email']
            password = request.POST['password']
            if(stuid == ''):
                usr = User(name=name, email=email, password=password)
            else:
                usr = User(id=stuid, name=name, email=email, password=password)
            usr.save()
            stud = User.objects.values()
            student_data = list(stud)
            return JsonResponse({'status':'Saved', 'student_data': student_data})
        else:
            return JsonResponse({'status':0})

def delete_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        pi = User.objects.get(pk=id)
        pi.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})

def edit_data(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(pk=id)
        student_data ={"id":student.id,"name":student.name,"email":student.email,"password":student.password}
        return JsonResponse(student_data)
        

