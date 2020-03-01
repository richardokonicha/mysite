from graphene import Schema, ObjectType
from polls.schema import Query as QuestionQuery
from ingredients.schema import Query as ingredientsQuery


class Query(QuestionQuery, ingredientsQuery, ObjectType):
    pass


schema = Schema(query=Query)
