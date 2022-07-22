from rest_framework import serializers

from .models import Post, Category, Author, Comments

class CategorySerializers(serializers.ModelSerializer):
    class Meta():
        model = Category
        fields = '__all__'

class PostSerializers(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = '__all__'

class AuthorSerializers(serializers.ModelSerializer):
    class Meta():
        model = Author
        fields = '__all__'

class CommentsSerializers(serializers.ModelSerializer):
    class Meta():
        model = Comments
        fields = '__all__'

class HomePageSerializers(serializers.ModelSerializer):
    region = Author
    post = PostSerializers
    category = CategorySerializers
    class Meta():
        model = Post
        fields = "__all__"