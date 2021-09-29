import graphene

import datasets.schema


class Query(datasets.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)