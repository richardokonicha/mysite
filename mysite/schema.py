from graphene import ObjectType, Schema
from ingredients.schema import Query as Q


class Query(Q, ObjectType):
    pass


schema = Schema(query=Query)
