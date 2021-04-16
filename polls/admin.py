from django.contrib import admin

from .models import QuestionModel, ChoiceModel
# Register your models here.


@admin.register(QuestionModel)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', )


@admin.register(ChoiceModel)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', )