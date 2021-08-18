from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post, Comment


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    # fields = ['title', 'author', 'body']
    fields = ['title', 'body']

    def form_valid(self, form): # Automatically pic author
        form.instance.author = self.request.user
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    # fields = ['title', 'author', 'body']
    fields = ['title', 'body']

    def form_valid(self, form): # Automatically pic author
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # Test if login user is the original post author
        obj = self.get_object()
        return obj.author == self.request.user


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):  # Test if login user is the original post author
        obj = self.get_object()
        return obj.author == self.request.user


class CommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    fields = ['post', 'comment']
    #fields = ['comment']

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.post = Post.get_object(Post._get_pk_val(self))
        #form.instance.post = self.
        return super().form_valid(form)
