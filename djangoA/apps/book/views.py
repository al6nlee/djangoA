from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializer


# 书视图类
class BookView(APIView):
    def get(self, requets):
        # 序列化
        book_list = models.Book.objects.all()
        # 序列化多条数据many=True
        ser = serializer.BookSerializer(instance=book_list, many=True)
        return Response(ser.data)

    def post(self, request):
        # 获取反序列化数据
        ser = serializer.BookSerializer(data=request.data)
        if ser.is_valid():
            # 校验通过存入数据库，不需要重写create方法了
            ser.save()
            return Response({'code': 100, 'msg': '新增成功', 'data': ser.data})
        # 校验失败
        return Response({'code': 101, 'msg': '校验未通过', 'error': ser.errors})


class BookViewDetail(APIView):
    def get(self, request, pk):
        book = models.Book.objects.filter(pk=pk).first()
        ser = serializer.BookSerializer(instance=book)
        return Response(ser.data)

    def put(self, request, pk):
        book = models.Book.objects.filter(pk=pk).first()
        # 修改，instance和data都要传
        ser = serializer.BookSerializer(instance=book, data=request.data)
        if ser.is_valid():
            # 校验通过修改，不需要重写update
            ser.save()
            return Response({'code:': 100, 'msg': '修改成功', 'data': ser.data})
        # 校验不通过
        return Response({'code:': 102, 'msg': '校验未通过，修改失败', 'error': ser.errors})

    def delete(self, request, pk):
        models.Book.objects.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})


# 作者视图类
class AuthorView(APIView):
    def get(self, requets):
        # 序列化
        author_list = models.Author.objects.all()
        # 序列化多条数据many=True
        ser = serializer.AuthorSerializer(instance=author_list, many=True)
        return Response(ser.data)

    def post(self, request):
        # 获取反序列化数据
        ser = serializer.AuthorSerializer(data=request.data)
        if ser.is_valid():
            # 校验通过存入数据库，不需要重写create方法了
            ser.save()
            return Response({'code': 100, 'msg': '新增成功', 'data': ser.data})
        # 校验失败
        return Response({'code': 101, 'msg': '校验未通过', 'error': ser.errors})


class AuthorViewDetail(APIView):
    def get(self, request, pk):
        book = models.Author.objects.filter(pk=pk).first()
        ser = serializer.AuthorSerializer(instance=book)
        return Response(ser.data)

    def put(self, request, pk):
        book = models.Author.objects.filter(pk=pk).first()
        # 修改，instance和data都要传
        ser = serializer.AuthorSerializer(instance=book, data=request.data)
        if ser.is_valid():
            # 校验通过修改，不需要重写update
            ser.save()
            return Response({'code:': 100, 'msg': '修改成功', 'data': ser.data})
        # 校验不通过
        return Response({'code:': 102, 'msg': '校验未通过，修改失败', 'error': ser.errors})

    def delete(self, request, pk):
        models.Author.objects.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})


# 作者详情视图类
class AuthorDetailView(APIView):
    def get(self, requets):
        # 序列化
        author_list = models.AuthorDetail.objects.all()
        # 序列化多条数据many=True
        ser = serializer.AuthorDetailSerializer(instance=author_list, many=True)
        return Response(ser.data)

    def post(self, request):
        # 获取反序列化数据
        ser = serializer.AuthorDetailSerializer(data=request.data)
        if ser.is_valid():
            # 校验通过存入数据库，不需要重写create方法了
            ser.save()
            return Response({'code': 100, 'msg': '新增成功', 'data': ser.data})
        # 校验失败
        return Response({'code': 101, 'msg': '校验未通过', 'error': ser.errors})


class OneAuthorViewDetail(APIView):
    def get(self, request, pk):
        book = models.AuthorDetail.objects.filter(pk=pk).first()
        ser = serializer.AuthorDetailSerializer(instance=book)
        return Response(ser.data)

    def put(self, request, pk):
        book = models.AuthorDetail.objects.filter(pk=pk).first()
        # 修改，instance和data都要传
        ser = serializer.AuthorDetailSerializer(instance=book, data=request.data)
        if ser.is_valid():
            # 校验通过修改，不需要重写update
            ser.save()
            return Response({'code:': 100, 'msg': '修改成功', 'data': ser.data})
        # 校验不通过
        return Response({'code:': 102, 'msg': '校验未通过，修改失败', 'error': ser.errors})

    def delete(self, request, pk):
        models.AuthorDetail.objects.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})


# 出版社视图类
class PublishView(APIView):
    def get(self, requets):
        # 序列化
        author_list = models.Publish.objects.all()
        # 序列化多条数据many=True
        ser = serializer.PublishSerializer(instance=author_list, many=True)
        return Response(ser.data)

    def post(self, request):
        # 获取反序列化数据
        ser = serializer.PublishSerializer(data=request.data)
        if ser.is_valid():
            # 校验通过存入数据库，不需要重写create方法了
            ser.save()
            return Response({'code': 100, 'msg': '新增成功', 'data': ser.data})
        # 校验失败
        return Response({'code': 101, 'msg': '校验未通过', 'error': ser.errors})


class PublishViewDetail(APIView):
    def get(self, request, pk):
        book = models.Publish.objects.filter(pk=pk).first()
        ser = serializer.PublishSerializer(instance=book)
        return Response(ser.data)

    def put(self, request, pk):
        book = models.Publish.objects.filter(pk=pk).first()
        # 修改，instance和data都要传
        ser = serializer.PublishSerializer(instance=book, data=request.data)
        if ser.is_valid():
            # 校验通过修改，不需要重写update
            ser.save()
            return Response({'code:': 100, 'msg': '修改成功', 'data': ser.data})
        # 校验不通过
        return Response({'code:': 102, 'msg': '校验未通过，修改失败', 'error': ser.errors})

    def delete(self, request, pk):
        models.Publish.objects.filter(pk=pk).delete()
        return Response({'code': 100, 'msg': '删除成功'})
