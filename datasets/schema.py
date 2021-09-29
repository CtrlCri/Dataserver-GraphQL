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

#1
class CreateDataset(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    about = graphene.String()

    #2
    class Arguments:
        title = graphene.String()
        about = graphene.String()

    #3
    def mutate(self, info, title, about):
        dataset = Dataset(title=title, about=about)
        dataset.save()

        return CreateDataset(
            id = dataset.id,
            title = dataset.title,
            about = dataset.about,
        )


#4
class Mutation(graphene.ObjectType):
    create_dataset = CreateDataset.Field()