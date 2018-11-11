from django.db import models


class Users(models.Model):
    user_name = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name


class Question(models.Model):
    question_text = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return self.question_text


class Response(models.Model):
    user_answer = models.TextField(default="No Answer")
    score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_name = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_answer
