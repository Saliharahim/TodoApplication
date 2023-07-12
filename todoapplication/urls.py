"""todoapplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from crm import views as crm_views
from django.conf import settings
from django.conf.urls.static import static
from crmapp import views as api_views
from rest_framework.routers import DefaultRouter
from todoapi import views as todo_views
from rest_framework.authtoken.views import ObtainAuthToken
router=DefaultRouter()

router.register("api/v1/employees",api_views.EmployeeViewsetView,basename="memployees")
router.register("api/users",todo_views.UserView,basename="users")
router.register("api/todos",todo_views.TodosView,basename="todos")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/add/',views.TodoCreateView.as_view(),name="todo-add"),
    path("todos/all/",views.TodoListView.as_view(),name="todo-list"),
    path("todos/<int:pk>",views.TodoDetailView.as_view(),name="todo-detail"),
    path("todos/<int:pk>/remove/",views.TodoDeleteView.as_view(),name="todo-delete"),
    path("todos/<int:pk>/change/",views.TodoEditView.as_view(),name="todo-update"),
    path('todos/complete/',views.TodoCompleteView.as_view(),name="todo-complete"),
    path("employees/add/",crm_views.EmployeeCreateView.as_view(),name="emp-add"),
    path("employees/all/",crm_views.EmployeeListView.as_view(),name="emp-list"),
    path("employees/<int:pk>/detail",crm_views.EmployeeDetailView.as_view(),name="emp-detail"),
    path("employees/<int:pk>/remove",crm_views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path('employees/<int:pk>/change/',crm_views.EmployeeEditView.as_view(),name="emp-edit"),
    path("register/",crm_views.SignUpView.as_view(),name="register"),
    path("login/",crm_views.SignInView.as_view(),name="signIn"),
    path('logout/',crm_views.signout_view,name="signout"),
    path('api/token/',ObtainAuthToken.as_view()),

    
    ]+router.urls+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
