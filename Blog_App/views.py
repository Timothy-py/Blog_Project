from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
from django.urls import reverse_lazy
from Blog_App.models import Post,Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from Blog_App.forms import PostForm,CommentForm
from django.views.generic import (TemplateView,ListView,DetailView,
                                    CreateView,UpdateView,DeleteView)
# from django.http import HttpRequest
# request=HttpRequest()
from django.contrib.auth.models import User
###################################
# Class Based Views
# Django CBV template naming convention
# <app>/<model>_<viewtype>.html
###################################

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    # ordering = ['-published_date']
    paginate_by = 3


class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    redirect_field_name = 'Blog_App/post_detail.html'
    form_class = PostForm
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    # login_url = '/login/'
    redirect_field_name = 'Blog_App/post_detail.html'
    form_class = PostForm
    model = Post

    def test_func(self):
        post_object = self.get_object()
        if self.request.user == post_object.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # success_url = reverse_lazy('Blog_App:post_list')
    success_url = '/'

    def test_func(self):
        post_object = self.get_object()
        if self.request.user == post_object.author:
            return True
        else:
            return False

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'Blog_App/post_list.html'
    template_name = 'Blog_App/post_draft_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('create_date')

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    redirect_field_name = 'Blog_App/post_detail.html'


###################################
# Function Based Views
###################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('Blog_App:post_detail',pk=pk)


def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment = form.save(commit=False)
            Comment.post = post
            Comment.save()
            return redirect('Blog_App:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'Blog_App/comment_form.html',{'form':CommentForm})




def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('Blog_App:post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('Blog_App:post_detail',pk=post_pk)

# def add_reply_to_comment(request,pk):
#     comment = get_object_or_404(Comment,pk=pk)
#     if request.method == 'POST':
#         replyform = ReplyForm(request.POST)
#         if replyform.is_valid():
#             Reply = replyform.save(commit=False)
#             Reply.comment = comment
#             Reply.save()
#             post_id = comment.post.pk
#             return redirect('Blog_App:post_detail', pk=post_id)
#     else:
#         replyform = ReplyForm()
#     return render(request, 'Blog_App/reply_form.html', {'form':ReplyForm})
