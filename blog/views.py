from django.shortcuts import render,redirect, get_object_or_404
from .forms import AddBlogForm,AddCommentForm
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# from .views import get_blog_queryset
from .models import BlogPost

BLOG_POSTS_PER_PAGE = 10
# Create your views here.

@csrf_exempt
def addblog(request):
    context = {}
    user = request.user
    if  user.is_authenticated:
        form = AddBlogForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj = form.save(commit=False)
            author = User.objects.filter(id=user.id).first()
            obj.author = author
            obj.save()
            form = AddBlogForm()

            context['form'] = form

    return render(request, "blog/addblog.html", context)

def detail_blog_view(request, pk):

	context = {}

	blog_post = get_object_or_404(BlogPost, pk=pk)
	context['blog_post'] = blog_post

	return render(request, 'blog/detail_blog.html', context)


def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ") # python install 2019 = [python, install, 2019]
	for q in queries:
		posts = BlogPost.objects.filter(
				Q(title__icontains=q) | 
				Q(body__icontains=q)
			).distinct()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))

def home_screen_view(request, *args, **kwargs):
	
	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('updated_on'), reverse=True)
	


	# Pagination
	page = request.GET.get('page', 1)
	blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	try:
		blog_posts = blog_posts_paginator.page(page)
	except PageNotAnInteger:
		blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	except EmptyPage:
		blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "blog/allblog.html", context)