from django.db import models
from users.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models. DateTimeField(auto_now=True)
    views = models.PositiveBigIntegerField(default=0, blank=True)
    tags = TaggableManager()

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('forum:question-detail', kwargs={'pk': self.pk})
    
    class Meta:
        ordering = ['-create_time']

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    


