import graphene
from blog.schema import Query, Mutation

schema = graphene.Schema(query=Query, mutation=Mutation)
