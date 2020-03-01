import graphene
from graphene_django.types import DjangoObjectType
from ingredients.models import Category, Ingredients


# TODO STEP1 first make an object type (DjangoObjectType) out of our models
class CategoryType(DjangoObjectType):
    class Meta:
        model = Category


class IngredientsType(DjangoObjectType):
    class Meta:
        model = Ingredients


# TODO STEP2 create Query class inherit object
# create List(Type) or Field(Type,*) types as fields in the Query class.
class Query(object):
    all_category = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientsType)

    category = graphene.Field(
        CategoryType,
        id=graphene.Int(),
        name=graphene.String()
        )

    ingredient = graphene.Field(
        IngredientsType,
        id=graphene.Int(),
        name=graphene.String()
        )

    # TODO resolve functions 
    def resolve_all_category(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwarg):
        return Ingredients.objects.all()
        # return Ingredients.objects.select_related('category').all

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Category.objects.get(pk=id)

        if name is not None:
            return Category.objects.get(name=name)

        return None

    def resolve_ingredients(self, info, **kwargs):
        id = kwargs.get('id')
        name = kwargs.get('name')

        if id is not None:
            return Ingredients.objects.get(pk=id)

        if name is not None:
            return Ingredients.objects.get(name=name)

        return None

# TODO then import module to project level schema