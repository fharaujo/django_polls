
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import QuestionModel, ChoiceModel


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'questions_list'
   
    def get_queryset(self):
        return QuestionModel.objects.filter(
            pub_date__lte=timezone.now()
            ).order_by('-pub_date')[:5]
         


class DetailView(generic.DetailView):
    model = QuestionModel
    template_name = 'detail.html'
    context_object_name = 'question'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return QuestionModel.objects.filter(pub_date__lte=timezone.now())
    


class ResultsView(generic.DetailView):
    model = QuestionModel
    template_name = 'results.html'
    context_object_name = 'question'


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



