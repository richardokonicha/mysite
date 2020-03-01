from graphene import Schema, ObjectType
from polls.schema.schema import Query as QuestionQ
from ingredients.schema.schema import Query as ingredientsQ
from ingredients.schema.schemaNode import Query as NodeQ


class Query(QuestionQ, NodeQ, ObjectType):
    pass


schema = Schema(query=Query)
