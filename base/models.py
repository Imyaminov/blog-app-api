from django.db import models
from basemodel import BaseModel
# Create your models here.

class Author(BaseModel):
    fullname = models.CharField(max_length=128)

    def __str__(self):
        return self.fullname

class Category(BaseModel):
    title = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    post_count = models.IntegerField(default=0)

    is_popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Post(BaseModel):
    title = models.CharField(max_length=128, verbose_name='Nomi')
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sub_content = models.TextField()

    author = models.ForeignKey(Author, related_name='posts')

    image = models.ImageField(upload_to="post/", null=True)
    published_date_time = models.DateTimeField(null=True)

    times_seen = models.IntegerField(default=0)
    read_duration = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    instagram_link = models.CharField(max_length=128, blank=True)
    twitter_link = models.CharField(max_length=128, blank=True)


    def __str__(self):
        return self.title

class Comments(BaseModel):
    title = models.CharField(max_length=128, verbose_name='Nomi')
    author = models.ForeignKey(Author, related_name='comments')
    content = models.TextField()
