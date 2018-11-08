from django.db import models


class Question(models.Model):
    sr_no = models.IntegerField(primary_key=True)
    question_text = models.TextField()
    answer = models.TextField()
    user_answer = models.TextField(default="Your answer")
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text
