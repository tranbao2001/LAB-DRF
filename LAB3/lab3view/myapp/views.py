from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_http_methods
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post, Article
from .forms import DocumentForm
from .models import Document
# Hàm xử lý cho trang chủ
def index(request):
    return render(request, 'index.html')

# Lưu trữ theo năm
def year_archive(request, year):
    posts = get_list_or_404(Post, created_at__year=year)
    return render(request, 'year_archive.html', {'posts': posts, 'year': year})

# Lưu trữ theo tháng
def month_archive(request, year, month):
    posts = get_list_or_404(Post, created_at__year=year, created_at__month=month)
    return render(request, 'month_archive.html', {'posts': posts, 'year': year, 'month': month})

# Chi tiết bài viết theo ID
@login_required  # Chỉ cho phép người dùng đã đăng nhập
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

# Tạo bài viết mới
@login_required
@permission_required('myapp.can_create_post', raise_exception=True)
@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(title=title, content=content)
        return redirect(post.get_absolute_url())
    return render(request, 'create_post.html')

# Liệt kê tất cả bài viết
def article_list(request):
    posts = Post.objects.all()  # Lấy tất cả bài viết
    return render(request, 'article_list.html', {'posts': posts})
def upload_file(request):
    if request.method == 'POST':
        # Xử lý dữ liệu từ biểu mẫu
        uploaded_file = request.FILES['file_field']
        new_file = ModelWithFileField(file_field=uploaded_file)
        new_file.save()
        return HttpResponseRedirect(reverse('post_detail', args=[new_file.id]))  # Redirect đến trang chi tiết file
    return render(request, 'upload.html')  # Render template cho upload

def upload_success(request):
    return render(request, 'upload_success.html')

