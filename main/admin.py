from django.contrib import admin

from .models import (
	Algo,
	Badges,
	Tags,
	Profile,
	Code
	)

admin.site.register(Algo)
admin.site.register(Badges)
admin.site.register(Tags)
admin.site.register(Profile)
admin.site.register(Code)
