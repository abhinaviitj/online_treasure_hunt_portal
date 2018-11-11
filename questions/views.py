from django.shortcuts import render, get_object_or_404
from .models import Users, Question, Response


# Create your views here.


def main(request):
    return render(request, 'questions/home.html')


def add_user(request):
    return render(request, 'questions/user.html')


def que_1(request, id):
    name = request.POST.get('user_name')
    u = Users(user_name=name)
    u.save()
    return question_detail(request, id, u.id)


def index(request, uid):
    question_list = Question.objects.order_by('id')
    user = get_object_or_404(Users, id=uid)
    context = {
        'question_list': question_list,
        'user': user,
    }
    return render(request, 'questions/index.html', context)


def question_detail(request, id, uid):
    user = get_object_or_404(Users, id=uid)
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return render(request, 'questions/index.html', {'user': user})
    context = {
        'question': question,
        'user': user,
    }
    return render(request, 'questions/question_detail.html', context)


def question_answer(request, uid, id):
    question = get_object_or_404(Question, id=id)
    user = get_object_or_404(Users, id=uid)
    user_ans = request.POST.get('user_answer')
    str1 = question.answer
    str2 = user_ans
    skore = 0
    if sorted(str1.lower()) == sorted(str2.lower()):
        skore = 1
    res = Response(user_answer=user_ans, score=skore, question=question, user_name=user)
    res.save()
    context = {
        'question': question,
        'res': res,
        'user': user,
    }
    return render(request, 'questions/answer.html', context)


def report(request, uid):
    question_list = Question.objects.order_by('id')
    user = get_object_or_404(Users, id=uid)
    response_list = Response.objects.filter(user_name_id=uid)
    context = {
        'question_list': question_list,
        'user': user,
        'response_list': response_list,
    }
    return render(request, 'questions/report.html', context)
