from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone', 'fam', 'name', 'otc']
    # def create(self, validated_data):
    #     user, created = User.objects.get_or_create(
    #         email=validated_data['email'],
    #         defaults={
    #             'phone': validated_data.get('phone', ''),
    #             'fam': validated_data.get('fam', ''),
    #             'name': validated_data.get('name', ''),
    #             'otc': validated_data.get('otc', ''),
    #         }
    #     )
    #     return user

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
        # fields = '__all__'
        fields = [
            'user', 'coords',
            'beautyTitle', 'title', 'other_titles', 'connect',
            'level_winter', 'level_summer', 'level_autumn', 'level_spring',
            'images'
        ]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        coords_data = validated_data.pop('coords')
        images_data = validated_data.pop('images')

        user, _ = User.objects.get_or_create(**user_data)
        coords, _ = Coords.objects.get_or_create(**coords_data)
        pereval = Added.objects.create(user=user, coords=coords, **validated_data)

        for image_data in images_data:
            Images.objects.create(pereval=pereval, **image_data)

        return pereval


class AddedSerializerUpdate(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta:
        model = Added
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.beauty_title = validated_data.get('beauty_title', instance.beauty_title)
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
        user.last_name = user_data.get('last_name', user.last_name)
        user.first_name = user_data.get('first_name', user.first_name)
        user.middle_name = user_data.get('middle_name', user.middle_name)
        user.phone = user_data.get('phone', user.phone)
        user.save()

        images_data = validated_data.get('attached_images', [])
        instance.attached_images.all().delete()
        for image_data in images_data:
            Images.objects.create(pereval=instance, **image_data)

        return instance


class AddedDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    images = ImagesSerializer(many=True)

    class Meta():
        model = Added
        fields = '__all__'