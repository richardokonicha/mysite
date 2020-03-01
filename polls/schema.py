import graphene
from graphene_django import DjangoObjectType
from polls.models import Question, Choice


# first assign graph type
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice


# TODO STEP2 create Query class inherit object
# create List(Type) or Field(Type,*) types as fields in the Query class.
class Query(object):
    all_questions = graphene.List(QuestionType)
    all_choices = graphene.List(ChoiceType)

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()
    
    def resolve_all_choices(self, info, **kwargs):
        return Choice.
