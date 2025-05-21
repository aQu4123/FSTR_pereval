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
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')
    status = serializers.CharField(read_only=True)

    class Meta:
        model = Added
        # fields = '__all__'
        fields = [
            'user', 'coords', 'status',
            'beautyTitle', 'title', 'other_titles', 'connect',
            'level_winter', 'level_summer', 'level_autumn', 'level_spring',
            'add_time', 'images'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        user, _ = User.objects.get_or_create(**user_data)
        coords= Coords.objects.create(**coords_data)
        pereval = Added.objects.create(user=user, coords=coords, **validated_data)

        for image_data in images_data:
            Images.objects.create(pereval=pereval, **image_data)

        return pereval


class AddedDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Added
        fields = [
            'user', 'coords', 'status',
            'beautyTitle', 'title', 'other_titles', 'connect',
            'level_winter', 'level_summer', 'level_autumn', 'level_spring',
            'add_time', 'images'
        ]

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.beautyTitle = validated_data.get('beautyTitle', instance.beautyTitle)
        instance.title = validated_data.get('title', instance.title)
        instance.other_titles = validated_data.get('other_titles', instance.other_titles)
        instance.connect = validated_data.get('connect', instance.connect)
        instance.level_spring = validated_data.get('level_spring', instance.level_spring)
        instance.level_summer = validated_data.get('level_summer', instance.level_summer)
        instance.level_autumn = validated_data.get('level_autumn', instance.level_autumn)
        instance.level_winter = validated_data.get('level_winter', instance.level_winter)
        instance.save()

        coords_data = validated_data.get('coords', {})
        coords = instance.coords
        coords.latitude = coords_data.get('latitude', coords.latitude)
        coords.longitude = coords_data.get('longitude', coords.longitude)
        coords.height = coords_data.get('height', coords.height)
        coords.save()

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

