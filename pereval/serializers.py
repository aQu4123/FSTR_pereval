from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fam', 'name', 'otc']


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ['latitude', 'longitude', 'height']


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['img', 'title']


class AddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Added
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        user = User.objects.create(**user_data)
        coords = Coords.objects.create(**coords_data)
        pereval = Added.objects.create(user=user, coords=coords, **validated_data)

        for image_data in images_data:
            Images.objects.create(pereval=pereval, **image_data)

        return pereval