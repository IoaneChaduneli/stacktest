from django.contrib import admin
from forum.models import Question, Answer

# Register your models here.
admin.site.register([
    Question,
    Answer,
])