from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404, render
from django.views import generic

from .forms import CommentForm
from .models import Post, Like, Property


def index(request):
    return render(request, 'blog/main.html')


def history(request):
    return render(request, 'blog/history.html')


def resources(request):
    return render(request, 'blog/resources.html')


class PostList(generic.ListView):
    paginate_by = 2
    queryset = Post.objects.filter(status='published').order_by('-publish')
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get(self, request, *args, **kwargs):
        comment_form = CommentForm()
        self.object = self.get_object()
        context = self.get_context_data(object=self.object, form=comment_form)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        post = self.get_object()

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Комментарий успешно добавлен')

        return redirect('blog:post_detail', slug=post.slug)


def like(request):
    id = request.GET['id']
    post = get_object_or_404(Post, id=id)
    like = Like.objects.filter(post=post, author=request.user).first()
    if like:
        like.delete()
    else:
        like = Like(post=post, author=request.user)
        like.save()
    return render(request, 'blog/widgets/like.html', {'post': post})


class PropertyList(generic.ListView):
    queryset = Property.objects.order_by('title')
    template_name = 'blog/property_list.html'


class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'blog/property_detail.html'