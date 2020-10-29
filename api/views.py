from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.core.exceptions import ValidationError

from .serializers import *

err_invalid_input = Response(
    {'message': 'Cannot create user, please recheck input fields'},
    status=status.HTTP_400_BAD_REQUEST,
)
err_no_permission = Response(
    {'message': 'You do not have permission to perform this action'},
    status=status.HTTP_403_FORBIDDEN,
)
err_not_found = Response(
    {'message': 'Not found'},
    status=status.HTTP_404_NOT_FOUND,
)
err_not_allowed = Response(
    {'message': 'Operation Not Allowed'},
    status=status.HTTP_405_METHOD_NOT_ALLOWED
)
err_internal_server_error = Response(
    {'message': 'Internal Server Error'},
    status=status.HTTP_500_INTERNAL_SERVER_ERROR
)

def check_arguments(request, args):
    # check for missing arguments
    missing = []
    for arg in args:
        if arg not in request:
            missing.append(arg)
    if missing:
        print(missing)
        response = {
            'Missing argument': '%s' % ', '.join(missing),
        }
        return 1, Response(response, status=status.HTTP_400_BAD_REQUEST)
    return 0,


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


    def create(self, request):
        response = check_arguments(request.data, ['text'])
        if response[0] != 0:
            return response[1]
        
        text = request.data['text']
        user = request.user
        try:
            post = Post.objects.create(text=text, user=user)
            return Response(
                {
                    'message': 'A post has been created',
                    'result': PostSerializer(post, many=False).data,
                },
                status=status.HTTP_200_OK
            )
        except:
            return err_internal_server_error


    @action(methods=['POST'], detail=True)
    def comment(self, request, pk=None):
        response = check_arguments(request.data, ['text'])
        if response[0] != 0:
            return response[1]
        try:
            post = Post.objects.get(id=int(pk))
        except:
            return err_not_found
        text = request.data['text']
        user = request.user

        try:
            comment = Comment.objects.create(post=post, text=text, user=user)
            return Response(
                {
                    'message': 'Your comment has been posted',
                    'results': CommentSerializer(comment, many=False).data
                },
                status=status.HTTP_200_OK
            )
        except:
            return err_internal_server_error

    @action(methods=['POST'], detail=True)
    def edit(self, request, pk=None):
        response = check_arguments(request.data, ['text'])
        if response[0] != 0:
            return response[1]

        try:
            post = Post.objects.get(id=int(pk))
        except:
            return err_not_found
        text = request.data['text']
        user = request.user

        if not user.is_staff and user != post.user:
            return err_no_permission

        try:
            post.text = text
            post.save()
            return Response(
                {
                    'message': 'The post has been edited',
                    'results': PostSerializer(post, many=False).data
                },
                status=status.HTTP_200_OK
            )
        except:
            return err_internal_server_error



class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(methods=['POST'], detail=True)
    def edit(self, request, pk=None):
        response = check_arguments(request.data, ['text'])
        if response[0] != 0:
            return response[1]
        try:
            comment = Comment.objects.get(id=int(pk))
        except:
            return err_not_found
        text = request.data['text']
        user = request.user

        if not user.is_staff and user != comment.user:
            return err_no_permission

        try:
            comment.text = text
            comment.save()
            return Response(
                {
                    'message': 'The comment has been edited',
                    'results': CommentSerializer(comment, many=False).data
                },
                status=status.HTTP_200_OK
            )
        except:
            return err_internal_server_error


            
 
