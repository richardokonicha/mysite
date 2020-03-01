import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from polls.models import Question, Choice


# import ipdb; ipdb.set_trace
# first assign graph type
class QuestionType(DjangoObjectType):
    class Meta:
        model = Question


class ChoiceType(DjangoObjectType):
    class Meta:
        model = Choice


# TODO STEP2 create Query class inherit object
# create List(Type) or Field(Type,*) types as fields in the Query class.
class Query(ObjectType):
    all_questions = graphene.List(QuestionType)
    question = graphene.Field(QuestionType, id=graphene.Int())
    choices = graphene.List(ChoiceType)

    def resolve_all_questions(self, info, **kwargs):
        return Question.objects.all()
    
    def resolve_choices(self, info, **kwargs):
        return Choice.objects.all().first()
    
    def resolve_question(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Question.objects.get(pk=id)
        return None
            

# write the mutations 