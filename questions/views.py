from django.shortcuts import render, get_object_or_404
from .models import Question


# Create your views here.


def main(request):
    question_list = Question.objects.order_by('sr_no')
    for question in question_list:
        question.score = 0
        question.user_answer = ""
        question.save()
    return render(request, 'questions/home.html')


def index(request):
    question_list = Question.objects.order_by('sr_no')
    context = {
        'question_list': question_list,
    }
    return render(request, 'questions/index.html', context)


def question_detail(request, sr_no):
    try:
        question = Question.objects.get(pk=sr_no)
    except Question.DoesNotExist:
        return render(request, 'questions/index.html')
    context = {
        'question': question,
    }
    return render(request, 'questions/question_detail.html', context)


def question_answer(request, sr_no):
    question = get_object_or_404(Question, pk=sr_no)
    question.user_answer = request.POST.get('user_answer')
    question.score = 0
    str1 = question.answer
    str2 = question.user_answer
    if sorted(str1.lower()) == sorted(str2.lower()):
        question.score = 1
    question.save()
    context = {
        'question': question,
    }
    return render(request, 'questions/answer.html', context)


def report(request):
    question_list = Question.objects.order_by('sr_no')
    context = {
        'question_list': question_list,
    }
    return render(request, 'questions/report.html', context)
