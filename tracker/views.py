from django.shortcuts import render

# Create your views here.


def trackOpenedPosts(request):
    postId = request.GET['post_id']
    userId = request.user.id
    