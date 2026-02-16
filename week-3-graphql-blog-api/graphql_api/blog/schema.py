import graphene
from graphene_django import DjangoObjectType   # connects Django models to GraphQL types
from .models import Author, Post

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ("id", "name")

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ("id", "title", "content", "author")

class Query(graphene.ObjectType):
    authors = graphene.List(AuthorType)
    posts = graphene.List(PostType)

    def resolve_authors(root, info):
        return Author.objects.all()

    def resolve_posts(root, info):
        return Post.objects.all() # Returns all posts from the database

class CreateAuthor(graphene.Mutation): #Defines a mutation
    author = graphene.Field(AuthorType)

    class Arguments: #Defines input fields for the mutation
        name = graphene.String(required=True)

    def mutate(self, info, name):# Runs when mutation is executed
        author = Author.objects.create(name=name)
        return CreateAuthor(author=author)

class CreatePost(graphene.Mutation): 
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.ID(required=True)

    def mutate(self, info, title, content, author_id):
        post = Post.objects.create(
            title=title,
            content=content,
            author_id=author_id
        )
        return CreatePost(post=post)

class Mutation(graphene.ObjectType): #Collects all mutations in one place
    create_author = CreateAuthor.Field()
    create_post = CreatePost.Field()
