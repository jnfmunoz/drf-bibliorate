from rest_framework import serializers
from booklist_app.models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data, *args, **kwargs):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Name and description cannot be the same.")
        elif data['name'] == data['author']:
            raise serializers.ValidationError("Name and author cannot be the same.")
        elif data['author'] == data['description']:
            raise serializers.ValidationError("Author and description cannot be the same.")
        else:
            return data
    
