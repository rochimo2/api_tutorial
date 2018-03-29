from rest_framework import serializers

from .models import Bucketlist

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the model instance into json format."""

    dueño = serializers.ReadOnlyField(source='dueño.username')

    class Meta:
        """Map this serializer to a model and their fields."""
        model = Bucketlist
        fields = ('id', 'deseo', 'dueño', 'fecha_creacion', 'fecha_modificacion')
        read_only_fields = ('fecha_creacion', 'fecha_modificacion')


class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    # bucketlists = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Bucketlist.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        # fields = ('id', 'username', 'bucketlists', 'password')
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            password = validated_data.pop('password', None)
            instance = self.Meta.model(**validated_data)
            if password is not None:
                instance.set_password(password)
            instance.save()
            return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance



    # def create(self, validated_data):
    #     user = super(UserSerializer, self).create(validated_data)
    #     password = make_password(validated_data['password'])
    #     user.set_password(password)
    #     user.save()
    #     return user

    # def update(self, validated_data):
    #     # instance.user = validated_data.get('user', instance.user)
    #     # instance.password = validated_data.get('password', instance.password)
    #     # instance.save()
    #     # return instance

    #     user = super(UserSerializer, self).update(validated_data)
    #     password = make_password(validated_data['password'])
    #     user.set_password(password)
    #     user.save()
    #     return user

