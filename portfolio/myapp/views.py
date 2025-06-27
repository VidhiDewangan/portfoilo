from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Student
from .froms import StudentForm

# Create your views here.
def homepage(request, id):
    xyz = Student.objects.all()
    context = {
         "data" : xyz,
    }
    return render(request, 'myapp/index.html', context)

def aboutUs(request):
    return HttpResponse("Hello, my name is vidhi!")



def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # save to DB
            return render(request, 'myapp/success.html')  # or redirect
    else:
        form = StudentForm()
    
    return render(request, 'myapp/student_form.html', {'form': form})
