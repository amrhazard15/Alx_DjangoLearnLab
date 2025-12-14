from rest_framework import viewsets, permissions, status, generics
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

User = get_user_model()
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def feed_view(request):
    following_users = request.user.following.all()
    user = request.user
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    
    if not created:
        return Response({"message": "You have already liked this post"}, status=status.HTTP_400_BAD_REQUEST)
    
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target=post
    )
    return Response({"message": "Post liked successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)

    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )

    if not created:
        return Response(
            {"message": "You have already liked this post"},
            status=status.HTTP_400_BAD_REQUEST
        )

    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb="liked your post",
        target=post
    )

    return Response({"message": "Post liked successfully"})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)

    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({"message": "Post unliked successfully"})
    except Like.DoesNotExist:
        return Response(
            {"message": "You have not liked this post"},
            status=status.HTTP_400_BAD_REQUEST
        )



