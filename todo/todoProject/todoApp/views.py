from django.shortcuts import render,redirect,get_object_or_404

from .models import toDoModel
from .forms import toDoForm
from django.contrib import messages

# Create your views here.


def home(request):
    todos = toDoModel.objects.all()  # Tüm görevleri al
    return render(request, 'todoApp/home.html', {'todos': todos})

def view_create(request):
      
      form=toDoForm()
      if request.method=="POST":
            form=toDoForm(request.POST)
            if form.is_valid():
                  form.save()
                  messages.success(request, "Görev başarıyla oluşturuldu.")
                  return redirect('todo_list')

      return render(request, 'todoApp/todo_form.html',{ "form":form})


def view_read(request):

      todo=toDoModel.objects.all()
      return render(request,'todoApp/todo_list.html',{'todo':todo})


def view_update(request, id):
    todo = get_object_or_404(toDoModel, id=id)
    if request.method == "POST":
        form = toDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()  # Kullanıcıyı atamadan kaydediyoruz
            messages.success(request, "Görev başarıyla güncellendi.")
            return redirect('todo_list')
    else:
        form = toDoForm(instance=todo)

    return render(request, 'todoApp/todo_update.html', {'todo': todo, 'form': form})
   




 

def view_delete(request,id):
      todo=get_object_or_404(toDoModel,id=id)

      if request.method=="POST":
            
      
            todo.delete()
            messages.info(request,"gorev silindi")
            return redirect('todo_list')
      return render(request, 'todoApp/todo_delete.html', {'todo': todo})

def view_list(request):
    todos = toDoModel.objects.all()
    return render(request, 'todoApp/todo_list.html', {'todos': todos})


def todo_add(request):
    form = toDoForm()
    if request.method == "POST":
        form = toDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Yönlendirme başarılıysa, veri de eklenmeli
        
    else:
        form = toDoForm()
    
    return render(request, 'toDoApp/todo_form.html', {'form': form})


def todo_list(request):
    todos = toDoModel.objects.all()  # Tüm görevleri getir
    print(todos)  # Konsola yazdır, gerçekten veri geliyor mu?
    return render(request, 'todoApp/todo_list.html', {'todos': todos})
                 
               