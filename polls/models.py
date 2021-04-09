from django.db import models

# Create your models here.
class QuestionModel(models.Model):
    question_text = models.CharField(verbose_name='Descrição', max_length=200)
    pub_date = models.DateTimeField(verbose_name='Data Publicação', auto_now_add=True)


    class Meta:
        verbose_name = 'Questão'
        verbose_name_plural = 'Questões'
        ordering = ['id']
    
    
    def __str__(self):
        self.question_text
    

class ChoiceModel(models.Model):
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name='Questão', max_length=200)
    votes = models.IntegerField(default=0)
