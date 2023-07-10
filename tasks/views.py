from django.shortcuts import render ,redirect
from django.views.generic import View
from django import forms
from tasks.models import Todo
from django.contrib import messages
# Create your views here.
class TodoForm(forms.Form):
    task_name=forms.CharField()
    # user=forms.CharField()

class TodoCreateView(View):
    def get(self,request,*args,**kw):
        form=TodoForm()
        return render(request,"todo-add.html",{"form":form})

    def post(self,request,*args,**kw):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todo.objects.create(**form.cleaned_data,user=request.user)
            messages.success(request,"todo has been created successfully")
            return redirect("todo-list")
        messages.error(request,"todo creatioin failed")
        return render(request,"todo-add.html",{"form":form})

class TodoListView(View):
    def get(self,request,*args,**kw):
        qs=Todo.objects.filter(status=False,user=request.user).order_by("-date")

        return render(request,"todo-list.html",{"todos":qs})

class TodoDetailView(View):
    def get(self,request,*args,**kw):
        id=kw.get("pk")
        qs=Todo.objects.get(id=id)
        return render(request,"todo-detail.html",{"todo":qs})

class  TodoDeleteView(View):
    def get(self,request,*args,**kw):
        id=kw.get("pk")
        Todo.objects.get(id=id).delete()
        messages.success(request,"todo has been deleted successfully")
        return redirect("todo-list")
    
class TodoEditView(View):
    def get(self,request,*args,**kw):
        id=kw.get("pk")
        Todo.objects.filter(id=id).update(status=True)
        messages.success(request,"todo has been changed")
        return redirect("todo-list")

class TodoCompleteView(View):
    def get(self,request,*args,**kw):
        qs=Todo.objects.filter(status=True)
        return render(request,"todo-complete.html",{"todos":qs})    