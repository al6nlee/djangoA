from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE)
    authors = models.ManyToManyField(to='Author')

    def __str__(self):
        return self.name

    # 自定制字段
    @property
    def publish_detail(self):
        return {'name': self.publish.name, 'addr': self.publish.city}

    @property
    def author_list(self):
        l = []
        print(self.authors.all())  # <QuerySet [<Author: Author object (1)>, <Author: Author object (2)>]>
        for author in self.authors.all():
            print(author.author_detail)  # AuthorDetail object (1)
            l.append({'name': author.name, 'age': author.age, 'addr': author.author_detail.addr})
        return l


class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    author_detail = models.OneToOneField(to='AuthorDetail', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @property
    def authordetail_info(self):
        return {'phone': self.author_detail.telephone, 'addr': self.author_detail.addr}


class AuthorDetail(models.Model):
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=64)


class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    email = models.EmailField()
