
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import QuestionModel, ChoiceModel


def index(request):
    questions_list = QuestionModel.objects.order_by('-pub_date')[:5]
    context = {'questions_list': questions_list}
    return render(request, 'index.html', context)

def detail(request, question_id):
    question = get_object_or_404(QuestionModel, id=question_id)
    return render(request, 'detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    try:
        selected_choice = question.choicemodel_set.get(pk=request.POST['choice'])
    except (KeyError, ChoiceModel.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Você não selecionou uma opção.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request, question_id):
    question = get_object_or_404(QuestionModel, pk=question_id)
    return render(request, 'results.html', {'question': question})