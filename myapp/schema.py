# myapp/schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import MyModel

class MyModelType(DjangoObjectType):
    class Meta:
        model = MyModel

class Query(graphene.ObjectType):
    my_model = graphene.Field(MyModelType, id=graphene.Int())

    def resolve_my_model(self, info, id):
        return MyModel.objects.get(pk=id)

schema = graphene.Schema(query=Query)
