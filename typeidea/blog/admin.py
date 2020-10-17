from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'is_nav', 'post_count', 'created_time')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = '文章数量'

    def save_model(self, request, obj, form, change):
        """重写 ModelAdmin 中此方法，直接fields 中加会引入更改作者的 bug"""
        obj.owner = request.user
        return super(CategoryAdmin, self).save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'created_time')
    fields = ('name', 'status')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(TagAdmin, self).save_model(request, obj, form, change)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'created_time', 'operator']
    list_display_links = []
    list_filter = ['category', ]
    search_fields = ['title', 'category__name']

    # actions_on_bottom = True

    # 编辑页面
    # save_on_top = True

    fields = (('category', 'title'), 'desc', 'status', 'content', 'tag', )

    def operator(self, obj):    # 自定义展示字段
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(PostAdmin, self).save_model(request, obj, form, change)
