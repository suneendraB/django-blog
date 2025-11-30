from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category


def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with id Category_id
    posts = Blog.objects.filter(status='Published', category=category_id)

    # #Use try/except when we want to do some custom action if the categoty doesn't exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     #redirect the use to the home page
    #     return redirect('home')

    # use get_object_or_404 when u want to show 404 error page if the category does not exist = 404 is default error page.
    
    
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category_id': category_id,
    }
    return render(request, 'posts_by_category.html', context)






