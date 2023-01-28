from rest_framework.serializers import ModelSerializer
from .models import *

class SocialPostSerializer(ModelSerializer):
    class Meta:
        model = SocialPost
        fields = '__all__'
