from rest_framework import serializers

from books.models import Books


class BooksOut(serializers.ModelSerializer):

    '''Serializer for data of books'''

    class Meta:

        '''Class init..s the serialized fields'''

        model = Books

        fields = [
                'pk',
                'title',
                'description',
                ]


class BooksIn(serializers.ModelSerializer):

    '''Serializer for data of books'''

    class Meta:

        '''Class init..s the serialized fields'''

        model = Books

        fields = [
                'title',
                'description',
                ]
