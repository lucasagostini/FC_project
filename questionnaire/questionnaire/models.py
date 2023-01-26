from django.db import models

class Question(models.Model):
    order = models.PositiveIntegerField()
    text = models.CharField(max_length=255)

    class Meta:
        app_label = 'questionnaire'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    
    class Meta:
        app_label = 'questionnaire'