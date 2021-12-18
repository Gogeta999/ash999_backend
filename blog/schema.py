import graphene

from graphene_django import DjangoObjectType
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from django.db.models import Q


from .models import Category, Post, Tag



#Should add below two lines cuz we use settings.auth_usermodel in models.py, so now we can call author in Post Type now
from django.contrib.auth import get_user_model
from django.conf import settings
User = get_user_model()

class UserType(DjangoObjectType):
    class Meta:
        model = User

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        exclude = ()

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        convert_choices_to_enum = ['publish_status']

class  TagNode(DjangoObjectType):
    class Meta:
        model = Tag
        filter_fields = {"name": ["exact", "icontains", "istartswith"]}
        fields = ("id", "name", "slug", "created_time", "last_modified_time")
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)

    all_categories= graphene.List(CategoryType)
    categories_by_name = graphene.List(CategoryType,  search=graphene.String(), first=graphene.Int(), skip=graphene.Int())
    
    tag = relay.Node.Field(TagNode)
    all_tags = DjangoFilterConnectionField(TagNode)

    def resolve_all_posts(root, info):
        # We can easily optimize query count in the resolve method
        return Post.objects.all()

    def resolve_all_categories(root, info):
        # We can easily optimize query count in the resolve method
        return Category.objects.filter(is_enable=True).all()
    def resolve_categories_by_name(root, info, search=None, first=None, skip=None, **kwargs):
        queryset = Category.objects.all()
        if search:
            filter = (
                Q(name__icontains=search)
                | Q(description__icontains=search)
            )
            queryset = queryset.filter(filter)

        if skip:
            queryset = queryset[skip:]

        if first:
            queryset = queryset[:first]  
        return queryset

schema = graphene.Schema(query=Query)