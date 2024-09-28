from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)  # Tiêu đề bài viết
    content = models.TextField()  # Nội dung bài viết
    created_at = models.DateTimeField(auto_now_add=True)  # Ngày tạo bài viết

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

class Article(models.Model):
    title = models.CharField(max_length=200)  # Tiêu đề bài viết
    content = models.TextField()  # Nội dung bài viết
    publish_date = models.DateTimeField()  # Ngày xuất bản

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[self.publish_date.year, self.publish_date.month, self.publish_date.day])
class Document(models.Model):
    title = models.CharField(max_length=100)  # Tiêu đề của tệp
    file = models.FileField(upload_to='documents/')  # Trường tệp

    def __str__(self):
        return self.title