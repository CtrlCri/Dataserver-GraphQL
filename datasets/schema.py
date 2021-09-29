import graphene
from graphene_django import DjangoObjectType

from .models import Dataset


class DatasetType(DjangoObjectType):
    class Meta:
        model = Dataset


class Query(graphene.ObjectType):
    datasets = graphene.List(DatasetType)

    def resolve_datasets(self, info, **kwargs):
        return Dataset.objects.all()