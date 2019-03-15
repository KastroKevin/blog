from django.contrib.auth import mixins
from django.shortcuts import redirect, render
from django.views import generic

from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
class PostList(mixins.LoginRequiredMixin, generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post/index.html'
    login_url = '/accounts/login'
    paginate_by = 3


class PostCreate(mixins.LoginRequiredMixin, generic.CreateView):
    queryset = Post
    form_class = PostForm
    template_name = 'post/new.html'
    success_url = '/publication/post'
    login_url = '/accounts/login'

    def post(self, request, *args, **kwargs):
        post = Post()
        post.user = request.user
        form = self.form_class(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('/publication/post')

        return render(request, self.template_name, {'form': self.form_class})


class CommentCreate(mixins.LoginRequiredMixin, generic.CreateView):
    queryset = Post
    form_class = CommentForm
    template_name = 'post/details.html'

    def get(self, request, *args, **kwargs):
        post = self.queryset.objects.get(id=kwargs['pk'])
        comentarios = post.comment_set.all()
        return render(request, self.template_name, {'post': post, 'form': self.form_class, 'comment': comentarios})

    def post(self, request, *args, **kwargs):
        post = self.queryset.objects.get(id=kwargs['pk'])
        comment = Comment()
        comment.user = request.user
        comment.post = post
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('/publication/post/' + str(post.id))

        return render(request, self.template_name, {'form': self.form_class, 'post':post})


class SeachPost(mixins.LoginRequiredMixin, generic.ListView):
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'post/busqueda.html'
    login_url = '/accounts/login'

    def get(self, request, *args, **kwargs):
        q = request.GET.get('q', '')
        return render(request, self.template_name, {'posts': self.queryset.filter(title__contains=q), 'q': q})


