from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import *

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/posts/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of posts'
        },
        {
            'Endpoint': '/posts/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single post object'
        },
        {
            'Endpoint': '/posts/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new post with data sent in post request'
        },
        {
            'Endpoint': '/posts/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing post with data sent in post request'
        },
        {
            'Endpoint': '/posts/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting post'
        },
    ]
    return Response(routes)


# /notes/<user_email> GET
# /notes/<user_email> POST
# /notes/<id> GET
# /notes/<id> PUT
# /notes/<id> DELETE


@api_view(['GET', 'POST'])
def getSocialPosts(request, user_email):

    if request.method == 'GET':
        return getSocialPostsList(request, user_email)

    if request.method == 'POST':
        return createSocialPost(request, user_email)


@api_view(['GET', 'PUT', 'DELETE'])
def getSocialPost(request, pk):

    if request.method == 'GET':
        return getSocialPostDetail(request, pk)

    if request.method == 'PUT':
        return updateSocialPost(request, pk)

    if request.method == 'DELETE':
        return deleteSocialPost(request, pk)
