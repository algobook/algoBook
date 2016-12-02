from registration.backends.default.views import RegistrationView
import datetime

from .models import Profile

class MyRegistrationView(RegistrationView):
    def register(self, request):
        new_user = super(MyRegistrationView, self).register(request)
        user_profile = Profile()
        user_profile.user = new_user
        user_profile.bio = ""
        user_profile.location = ""
        user_profile.birth_date = datetime.datetime(1947, 8, 15)
        user_profile.save()
        return user_profile
