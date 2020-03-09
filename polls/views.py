# from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from polls.models import Question


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
    return HttpResponse("You're voting on %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)
