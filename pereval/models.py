from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    phone = models.CharField(max_length=15, verbose_name='Телефонный номер')
    fam = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    otc = models.CharField(max_length=100, blank=True, verbose_name='Отчество')

    def __str__(self):
        return f"{self.fam} {self.name}"

class Coords(models.Model):
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')
    height = models.FloatField(verbose_name='Высота')

    def __str__(self):
        return f"Широта: {self.latitude}, Долгота: {self.longitude}, Высота: {self.height}"


class Added(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('pending', 'На модерации'),
        ('accepted', 'Принята'),
        ('rejected', 'Отклонена'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='new')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coords, on_delete=models.CASCADE)

    beautyTitle = models.CharField(max_length=100, verbose_name='Тип местности')
    title = models.CharField(max_length=100, verbose_name='Название')
    other_titles = models.CharField(max_length=100, verbose_name='Другие названия')
    connect = models.TextField(blank=True, verbose_name='Сопроводительный текст')
    add_time = models.DateTimeField(auto_now_add=True)

    level_winter = models.CharField(max_length=5, blank=True, verbose_name='Уровень сложности зимой')
    level_summer = models.CharField(max_length=5, blank=True, verbose_name='Уровень сложности летом')
    level_autumn = models.CharField(max_length=5, blank=True, verbose_name='Уровень сложности осенью')
    level_spring = models.CharField(max_length=5, blank=True, verbose_name='Уровень сложности весной')

    def __str__(self):
        return f"Перевал: {self.title}, Статус: {self.status}"


class Images(models.Model):
    pereval = models.ForeignKey('Added', on_delete=models.CASCADE, related_name='images')
    img = models.URLField()
    title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} - {self.img}"
