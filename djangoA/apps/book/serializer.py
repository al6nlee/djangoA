from . import models
from rest_framework import serializers


# 书序列化器
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定和哪个表有关系
        model = models.Book
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'publish', 'authors', 'publish_detail', 'author_list']
        # 将关联表的信息全部取出来，不推荐使用
        # depth = 1

        extra_kwargs = {
            'publish': {'write_only': True},
            'authors': {'write_only': True}
        }


# 作者序列化器
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定和哪个表有关系
        model = models.Author
        # fields = '__all__'
        fields = ['id', 'name', 'age', 'author_detail', 'authordetail_info']
        extra_kwargs = {
            'author_detail': {'write_only': True},
        }


# 作者详情序列化器
class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定和哪个表有关系
        model = models.AuthorDetail
        fields = '__all__'


# 出版社序列化器
class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        # 指定和哪个表有关系
        model = models.Publish
        fields = '__all__'
