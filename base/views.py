from django.shortcuts import render
from .models import Post, Category, Comments, Author

from rest_framework import generics


from .serializers import PostSerializers, CategorySerializers, CommentsSerializers, HomePageSerializers,  AuthorSerializers

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_popular=True)
    serializer_class = HomePageSerializers

class RecentPostAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by("-published_date")
    serializer_class = HomePageSerializers

class PopularPostAPIView(generics.ListAPIView):
    queryset = Post.objects.order_by("-published_date")
    serializer_class = HomePageSerializers

class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'

class CommentsToPostsDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id' # post id