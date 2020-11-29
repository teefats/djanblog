
from django.shortcuts import render
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
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})

def contact_us(request):
    return render(request, 'blog/contact_us.html', {'title': 'Contact us'})