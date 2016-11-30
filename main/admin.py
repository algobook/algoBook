from django.contrib import admin

from .models import (
	Algo,
	Badges,
	Tags,
	MyUser
	)

admin.site.register(Algo)
admin.site.register(Badges)
admin.site.register(Tags)
admin.site.register(MyUser)
