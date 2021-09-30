import graphene
from graphene_django import DjangoObjectType

from .models import Dataset, Like
from users.schema import UserType

from graphql import GraphQLError

class DatasetType(DjangoObjectType):
    class Meta:
        model = Dataset

class LikeType(DjangoObjectType):
    class Meta:
        model = Like

class Query(graphene.ObjectType):
    datasets = graphene.List(DatasetType)
    likes = graphene.List(LikeType)

    def resolve_datasets(self, info, **kwargs):
        return Dataset.objects.all()

    def resolve_likes(self, info, **kwargs):
        return Like.objects.all()

# Add the CreateDataset mutation
class CreateDataset(graphene.Mutation):
    id = graphene.Int()
    title = graphene.String()
    about = graphene.String()
    posted_by = graphene.Field(UserType)

    class Arguments:
        title = graphene.String()
        about = graphene.String()

    def mutate(self, info, title, about):
        user = info.context.user or None

        dataset = Dataset(
            title=title, 
            about=about,
            posted_by=user)
        dataset.save()

        return CreateDataset(
            id = dataset.id,
            title = dataset.title,
            about = dataset.about,
            posted_by = dataset.posted_by,
        )
# Add the CreateLike mutation
class CreateLike(graphene.Mutation):
    user = graphene.Field(UserType)
    dataset = graphene.Field(DatasetType)

    class Arguments:
        dataset_id = graphene.Int()

    def mutate(self, info, dataset_id):
        user = info.context.user
        if user.is_anonymous:
            raise GraphQLError('You must be logged to like!') #Exception('You must be logged to like!')

        dataset = Dataset.objects.filter(id=dataset_id).first()
        if not dataset:
            raise Exception('Invalid Dataset!')

        Like.objects.create(
            user=user,
            dataset=dataset,
        )

        return CreateLike(user=user, dataset=dataset)

class Mutation(graphene.ObjectType):
    create_dataset = CreateDataset.Field()
    create_like = CreateLike.Field()

