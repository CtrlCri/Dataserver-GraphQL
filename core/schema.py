import graphene

import datasets.schema


class Query(datasets.schema.Query, graphene.ObjectType):
    pass

class Mutation(datasets.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)