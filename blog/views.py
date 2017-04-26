from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Post
from .forms import PostForm

class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Post.objects.order_by('-timeposted')[:5]

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

