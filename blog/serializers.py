from rest_framework import serializers
from .models import Blogpost

class BlogpostSerializer(serializers.ModelSerializer):

    content = serializers.SerializerMethodField()

    def get_content(self, instance):
        return f"{instance.body_1} {instance.body_2} {instance.body_3} {instance.body_4} {instance.body_5} {instance.body_6}"

    class Meta:
        model = Blogpost
        fields = (
            'title',
            'content',
            'author',
            'date',
        )

    
       