from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.db.models import Count, F
from django.views.generic import CreateView, ListView
from django.views.generic.base import View
from django.views.generic.detail import DetailView

from .models import Post
from .forms import CommentForm, PostCreateForm


class Index(ListView):
    """Главная страница, вывод последних 10 постов"""
    queryset = Post.objects.filter(draft=False).select_related('author')
    context_object_name = 'posts'
    template_name = 'main/index.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Post.tags.annotate(Count('post')).order_by('-post__count')[:5]
        return context


class PostDetail(DetailView):
    """Вывод одного конкретного поста"""
    queryset = Post.objects.filter(draft=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Post.tags.all()
        # context['comments'] = Post.comment_set.all()
        return context


class AddComment(LoginRequiredMixin, View):
    """Форма для добавления комментария"""
    def post(self, request, pk):
        form = CommentForm(request.POST)
        post = Post.objects.get(id=pk)
        user = request.user.id
        if form.is_valid():
            form = form.save(commit=False)
            form.author_id = user
            form.post_id = pk
            form.save()
        return redirect(post.get_absolute_url())


class PostCreate(LoginRequiredMixin, CreateView):
    """Создание поста"""
    template_name = 'main/post_create.html'
    form_class = PostCreateForm








