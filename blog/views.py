from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import BlogPost, BlogPostImage
from .serializers import BlogPostSerializer, UserSerializer


class RegisterUserView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all().order_by('-created_at')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly]

    @action(detail=True, methods=['get'], url_path='increment-views', url_name='increment_views')
    def increment_views(self, request, slug=None):
        post = self.get_object()
        BlogPost.objects.filter(pk=post.pk).update(views=post.views+1)
        return Response({'message': 'Views updated', 'views': post.views + 1})

    def create(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        blog_post = serializer.save(author=self.request.user)

        for image in images:
            BlogPostImage.objects.create(blog_post=blog_post, image=image)

        return Response(BlogPostSerializer(blog_post).data, status=status.HTTP_201_CREATED)