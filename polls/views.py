# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from polls.models import Question, Choice


# Create your views here.
def index(request):
    list_of_objects = Question.objects.order_by('-pub_date')[:5]
    # output = '<div><br><br></div>'.join([str(i) for i in list_of_objects])
    context = {
        "list_of_objects": list_of_objects
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question
    }
    return render(request, 'polls/detail.html', context)


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {
        "question": question,
        "error_message": "You didn't select a choice"
    }
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    all_choices = question.choice_set.all()
    context = {
        "choices": all_choices
    }
    return render(request, "polls/results.html", context)
