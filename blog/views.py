from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog
from .serializers import BlogSerializer


class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]

    # Enable filters, ordering, and search
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]

    # Filter by these fields: ?author=1 or ?title=Some
    filterset_fields = ['author', 'title']

    # Search by: ?search=something
    search_fields = ['title', 'content']

    # Order results by: ?ordering=created_at or ?ordering=title
    ordering_fields = ['created_at', 'title']

    # Make the logged-in user as author
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
