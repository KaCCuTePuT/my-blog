from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )


class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'title', 'text', 'img', 'tags')

