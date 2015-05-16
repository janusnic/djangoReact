from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Comment
from rest_framework import status
from rest_framework import viewsets
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    # Queryset we wont our list to use
    queryset = Comment.objects.all()
    # The serializer we created for all the data
    serializer_class = CommentSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Get a list of objects after the comment is created
        serializer2 = self.get_serializer(queryset, many=True)

        # Return a list of comments instead of the comment
        return Response(serializer2.data)

        # headers = self.get_success_headers(serializer.data)

        # return Response(serializer.data, status=status.HTTP_201_CREATED,
        #                 headers=headers)
