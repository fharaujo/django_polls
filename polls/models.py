import datetime
from django.db import models

from django.utils import timezone

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(verbose_name='Descrição', max_length=200)
    pub_date = models.DateTimeField(verbose_name='Data Publicação', auto_now_add=True)


    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
    
    def publicado_recente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.question_text
    

class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    class Meta:
        verbose_name = 'Escolha'
        verbose_name_plural = 'Escolhas'
    
    def __str__(self):
        return self.choice_text