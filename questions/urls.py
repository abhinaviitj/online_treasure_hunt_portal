from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('<int:uid>/', views.index, name='index'),
    path('<int:uid>/<int:id>/', views.question_detail, name='question_detail'),
    path('<int:uid>/<int:id>/answer/', views.question_answer, name='question_answer'),
    path('<int:uid>/report/', views.report, name='report'),
    path('user/', views.add_user, name='add_user'),
    path('user/<int:id>/', views.que_1, name='que_1')
]
