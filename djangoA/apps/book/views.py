from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin, RetrieveModelMixin, \
    UpdateModelMixin

from . import models
from . import serializer


# 书视图类
class BookView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class BookViewDetail(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 作者
class AuthorView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializer.AuthorSerializer

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class AuthorViewDetail(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = models.Author.objects.all()
    serializer_class = serializer.AuthorSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 作者详情

class AuthorDetailView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = models.AuthorDetail.objects.all()
    serializer_class = serializer.AuthorDetailSerializer

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class OneAuthorViewDetail(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = models.AuthorDetail.objects.all()
    serializer_class = serializer.AuthorDetailSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


# 出版社
class PublishView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = serializer.PublishSerializer

    def get(self, request):
        return super().list(request)

    def post(self, request):
        return super().create(request)


class PublishViewDetail(RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = models.Publish.objects.all()
    serializer_class = serializer.PublishSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
