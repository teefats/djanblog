
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post

# posts = [{
#     'author' : 'Rudolf',
#     'title' : 'Hess',
#     'content' : 'First post',
#     'date_posted' : 'April 3, 2020'
# },{
#     'author' : 'Paul',
#     'title' : 'Kesselring',
#     'content' : 'Second post',
#     'date_posted': 'June 1 , 2020'
# }]

# Create your views here.
# def home(request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    #<app>/<model><viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # template_name = 'blog/home.html'
    # #<app>/<model><viewtype>.html
    # context_object_name = 'posts'
    # ordering = ['-date_posted']
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,
                    UserPassesTestMixin,
                    DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def contact_us(request):
    return render(request, 'blog/contact_us.html', {'title': 'Contact us'})