from rest_framework.response import Response
from .models import *
from .serializers import *
from django.contrib.auth import get_user_model
User = get_user_model()
 
 
def getSocialPostsList(request, user_email):
    posts = SocialPost.objects.filter(author__email=user_email).order_by('-updated')
    print(posts)
    serializer = SocialPostSerializer(posts, many=True)
    return Response(serializer.data)


def getSocialPostDetail(request, pk):
    post = SocialPost.objects.get(id=pk)
    print(post)
    serializer = SocialPostSerializer(post, many=False)
    return Response(serializer.data)


def createSocialPost(request, user_email):
    data = request.data
    author = User.objects.get(email=user_email)
    new_post = SocialPost.objects.create(
        author=author,
        post_body=data['body'],
    )
    serializer = SocialPostSerializer(new_post, many=False)
    return Response(serializer.data)

def updateSocialPost(request, pk):
    data = request.data
    post = SocialPost.objects.get(id=pk)
    serializer = SocialPostSerializer(instance=post, data=data)

    if serializer.is_valid():
        serializer.save()

    return serializer.data


def deleteSocialPost(request, pk):
    post = SocialPost.objects.get(id=pk)
    post.delete()
    return Response('Your post was deleted!')
