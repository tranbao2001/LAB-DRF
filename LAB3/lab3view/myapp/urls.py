from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Trang chủ
    path('articles/<int:year>/', views.year_archive, name='year_archive'),  # Lưu trữ theo năm
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month_archive'),  # Lưu trữ theo tháng
    path('posts/<int:id>/', views.post_detail, name='post_detail'),  # Chi tiết bài viết theo ID
    path('create/', views.create_post, name='create_post'),  # Tạo bài viết mới
    path('article_list/', views.article_list, name='article_list'),  # Liệt kê bài viết
    path('upload/', views.upload_file, name='upload_file'),  # Đường dẫn cho upload
]
