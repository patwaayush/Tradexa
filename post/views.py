from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.core.exceptions import ValidationError
# Create your views here.



@login_required
def index(request):

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            Post(user=request.user, text=form.cleaned_data['text_field']).save()
            return redirect('newsfeed')
        raise ValidationError("Please enter 10 char min")
    context = {
        'postForm': PostForm()
    }
    return render(request,'index.html',context=context)


def newsfeed(request):
    post = Post.objects.all()
    return render(request, 'newsfeed.html', {'posts':post})
