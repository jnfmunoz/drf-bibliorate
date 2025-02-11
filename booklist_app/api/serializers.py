from rest_framework import serializers
from booklist_app.models import Editorial, Book

class EditorialSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Editorial
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):

    editorial = serializers.CharField(source='editorial.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'editorial', 'synopsis', 'created']

    def validate(self, data, *args, **kwargs):
        if data['title'] == data['synopsis']:
            raise serializers.ValidationError("Title and synopsis cannot be the same.")
        elif data['title'] == data['author']:
            raise serializers.ValidationError("Title and author cannot be the same.")
        elif data['author'] == data['synopsis']:
            raise serializers.ValidationError("Author and synopsis cannot be the same.")
        else:
            return data
