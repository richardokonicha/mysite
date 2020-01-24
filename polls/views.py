# from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import render


# Create your views here.
def index(request):
    list_of_objects = Question.objects.order_by('-pub_date')
    # output = '<div><br><br></div>'.join([str(i) for i in list_of_objects])
    context = {
        "list_of_objects": list_of_objects
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    return HttpResponse("This is the detail view for the value ==> {}".format(question_id))


def vote(request, question_id):
    return HttpResponse("This is the vote view")


def results(request, question_id):
    return HttpResponse("this is the results views for {}".format(question_id))
