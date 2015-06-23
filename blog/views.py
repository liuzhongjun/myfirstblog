from django.shortcuts import render

# Create your views here.

# lets put a simplest view by Django girls.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
