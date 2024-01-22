from django.shortcuts import render,redirect, get_list_or_404, get_object_or_404
from django.views.generic import View
from .forms import PostCreateForm
from .models import Post
# Create your views here.
class BlogLisView(View):
    def get(self,request,*args,**kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts
        }
        return render(request,'blog_list.html',context)
    

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        # Obtenemos los campos que declaramos en el modelo
        form = PostCreateForm()  # Llama al formulario para instanciarlo
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                tittle = form.cleaned_data.get("tittle")
                content = form.cleaned_data.get("content")

                p, created = Post.objects.get_or_create(tittle=tittle, content=content)
                p.save()
                return redirect("blog:home")

        context = {}
        return render(request, "blog_create.html", context)


class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post': post
        }
        return render(request, 'blog_detail.html', context)