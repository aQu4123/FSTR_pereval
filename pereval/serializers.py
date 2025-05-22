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
        fields = ['data', 'title']


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ['winter', 'summer', 'autumn', 'spring']


class AddedSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Added
        fields = [
            'id', 'user', 'coords', 'level', 'status',
            'beautyTitle', 'title', 'other_titles', 'connect',
            'add_time', 'images'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')
        level_data = validated_data.pop('level')
        user, _ = User.objects.get_or_create(**user_data)
        coords= Coords.objects.create(**coords_data)
        level= Level.objects.create(**level_data)
        pereval = Added.objects.create(user=user, coords=coords, level=level, **validated_data)

        for image_data in images_data:
            Images.objects.create(pereval=pereval, **image_data)

        return pereval


class AddedDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Added
        fields = [
            'user', 'coords', 'status', 'level',
            'beautyTitle', 'title', 'other_titles', 'connect',
            'add_time', 'images'
        ]

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.beautyTitle = validated_data.get('beautyTitle', instance.beautyTitle)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.save()

        coords_data = validated_data.get('coords', {})
        coords = instance.coords
        coords.latitude = coords_data.get('latitude', coords.latitude)
        coords.longitude = coords_data.get('longitude', coords.longitude)
        coords.height = coords_data.get('height', coords.height)
        coords.save()

        level_data = validated_data.get('level', {})
        level = instance.level
        level.autumn = level_data.get('autumn', {})
        level.spring = level_data.get('spring', {})
        level.summer = level_data.get('summer', {})
        level.winter = level_data.get('winter', {})
        level.save()

        user_data = validated_data.get('user', {})
        user = instance.user
        user.email = user_data.get('email', user.email)
        user.fam = user_data.get('fam', user.fam)
        user.name = user_data.get('name', user.name)
        user.otc = user_data.get('otc', user.otc)
        user.phone = user_data.get('phone', user.phone)
        user.save()

        images_data = validated_data.get('images', [])
        instance.images.all().delete()
        for image_data in images_data:
            Images.objects.create(pereval=instance, **image_data)

        return instance

