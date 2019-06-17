from django.shortcuts import render, get_object_or_404
from . models import Post, Category
# Create your views here.

def blog (request):
    posts = Post.objects.all()
    return render (request,"blog/blog.html",{'posts':posts})

def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    category = get_object_or_404(Category, id= category_id)
    #posts = Post.objectss.filter(categories=category)  cambiado por template tag category.get_posts.all es una relacion inversa
    return render(request,"blog/category.html",{'category':category})


