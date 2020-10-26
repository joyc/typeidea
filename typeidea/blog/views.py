from django.shortcuts import render
from django.views.generic import ListView, DetailView

from config.models import SideBar
from .models import Post, Category


# 改为 class based view - ListView
def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        post_list, tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list, category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_nav())
    return render(request, 'blog/list.html', context=context)


class PostListView(ListView):
    queryset = Post.latest_posts()
    paginate_by = 1  # 分页设置的每页数量
    context_object_name = 'post_list'  # 如果不设置则在模板中要使用 object_list 变量
    template_name = 'blog/list.html'

# 改为 class based view - DetailView
# def post_detail(request, post_id=None):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         post = None
#     context = {
#         'post': post,
#         'sidebars': SideBar.get_all(),
#     }
#     context.update(Category.get_nav())
#
#     return render(request, 'blog/detail.html', context=context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
