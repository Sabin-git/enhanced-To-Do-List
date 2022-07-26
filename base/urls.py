from django.urls import path
from .views import TaskDelete, TaskList, TaskCreate, TaskUpdate, TaskDelete, UserLogin, UserRegister, TaskComplete
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', UserRegister.as_view(), name='register'),

    path('', TaskList.as_view(), name='tasks'),
    path('newtask/', TaskCreate.as_view(), name='newtask'),
    path('edit/<int:pk>/', TaskUpdate.as_view(), name='edit'),
    path('delete/<int:pk>/', TaskDelete.as_view(), name='delete'),
    path('complete/<int:pk>/', TaskComplete.as_view(), name='complete')    
] 