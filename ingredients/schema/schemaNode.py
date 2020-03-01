from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from ingredients.models import Category, Ingredients


# Graphene will automatically map the category model field into the categoryNOde 
# fields this is configured in the CategoryNode's Meta class

class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ['name', 'ingredients']
        interfaces = (relay.Node, )


class IngredientsNode(DjangoObjectType):
    class Meta:
        model = Ingredients
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'note': ['exact', 'icontains'],
            'category': ['exact']
        }
        interfaces = (relay.Node,)


class Query(ObjectType):
    category = relay.Node.Field(CategoryNode)
    all_category = DjangoFilterConnectionField(CategoryNode)

    ingredients = relay.Node.Field(IngredientsNode)
    all_ingredients =  DjangoFilterConnectionField(IngredientsNode)