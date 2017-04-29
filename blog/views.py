from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-timeposted')

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timeposted = timezone.now()
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
