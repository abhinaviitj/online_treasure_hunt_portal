from django.urls import path
from . import views

app_name = 'questions'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sr_no>/', views.question_detail, name='question_detail'),
    path('<int:sr_no>/answer/', views.question_answer, name='question_answer'),
    path('report/', views.report, name='report')
]
