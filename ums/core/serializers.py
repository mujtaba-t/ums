from djoser.serializers import UserSerializer
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from management.models import Recruiter

class UserSerializer(UserSerializer):
    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ('user_type', 'user_id')

class UserCreateSerializer(UserCreateSerializer):
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        last_instance = Recruiter.objects.latest('id')
        id_of_last_instance = last_instance.id
        return id_of_last_instance

    class Meta(UserCreateSerializer.Meta):
        fields = UserCreateSerializer.Meta.fields + ('user_type', 'user_id')