from django.http import HttpResponse
from django.http import  HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone

from django.shortcuts import get_object_or_404, render
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:20]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def get_queryset(self):
    """
    Return the last five published questions (not including those set to be
    published in the future).
    """
    return Question.objects.filter(
    pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:20]

def create(request):
    
    context = {}
    if request.method == "POST":
        question = Question.objects.create(question_text=request.POST['question_name'],pub_date=request.POST['pub_date'])
        Choice.objects.create(question=question,choice_text = request.POST['choice3'],votes = 0)
        Choice.objects.create(question=question,choice_text = request.POST['choice1'],votes = 0)
        Choice.objects.create(question=question,choice_text = request.POST['choice2'],votes = 0)
         
        return redirect('/polls/')

    return render(request,'create.html',context)