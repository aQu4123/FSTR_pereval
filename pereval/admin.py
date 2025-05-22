from django.contrib import admin
from .models import User, Added, Coords, Images, Level


admin.site.register(User)
admin.site.register(Added)
admin.site.register(Coords)
admin.site.register(Images)
admin.site.register(Level)
