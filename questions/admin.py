from django.contrib import admin
from .models import Question, Users, Response

admin.site.register(Question)
admin.site.register(Users)
admin.site.register(Response)
