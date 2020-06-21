from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from django.contrib import admin
from .models import Post, Comment


class PostAdminForm(forms.ModelForm):
    text = forms.CharField(label='Содержание', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('id', 'title', 'author', 'slug', 'draft', 'date')
    list_display_links = ('title', )
    save_on_top = True
    list_filter = ('author', 'date')
    search_fields = ('title', 'text')
    readonly_fields = ('slug', )
    list_editable = ('draft',)
    fieldsets = (
        (None, {
            'fields': (('title', 'slug', 'text'), )
        }),
        (None, {
            'fields': (('author', 'img', 'tags', 'draft'), )
        }),

    )
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'date', 'active')
    list_display_links = ('post', )
    list_editable = ('active', )




