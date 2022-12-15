from django.shortcuts import render, HttpResponseRedirect
from .models import issue_book
from .forms import StudentsForm,Issue_book
from django.contrib import messages


def home(request):
    return(render(request, 'home.html'))


def student(request):
    if request.method=="POST":
        form1 = StudentsForm(request.POST)
        if form1.is_valid():
            form1.save()
    else:
        form1 = StudentsForm
    return render(request, 'contact_forms.html', {'form1':form1})

def aboutus(request):
    return(render(request, 'about_us.html'))



def details(request):
    if request.method == 'POST':
        fm = Issue_book(request.POST)
        if fm.is_valid():
            stu = fm.cleaned_data['student']
            bt = fm.cleaned_data['book_title']
            ba = fm.cleaned_data['book_author']
            id=fm.cleaned_data['issue_date']

            reg = issue_book(student=stu, book_author=ba, book_title=bt,issue_date=id)
            reg.save()
            fm =Issue_book()
            messages.add_message(request, messages.SUCCESS, 'you added data successfully !!!')

    else:
        fm = Issue_book()
    stud = issue_book.objects.all()
    return render(request, 'details_page.html', {'form2':fm, 'stu':stud})


def update_data(request,id):
    if request.method == 'POST':
        pi = issue_book.objects.get(pk=id)
        fm = Issue_book(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            messages.add_message(request, messages.SUCCESS, 'you updated data successfully !!!')
            messages.info(request, 'you can go back !!!')
    else:
        pi =issue_book.objects.get(pk=id)
        fm = Issue_book(instance=pi)

    return render(request, 'update.html', {'form3': fm})


def delete_data(request,id):
    if request.method == 'POST':
        pi = issue_book.objects.get(pk=id)
        pi.delete()
        v=messages.info(request, 'Deleted !!!')
        return HttpResponseRedirect('/details/')

