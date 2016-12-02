from registration.backends.default.views import RegistrationView

from .models import Profile

class MyRegistrationView(RegistrationView):
    def register(self, request):
        new_user = super(MyRegistrationView, self).register(request)
        user_profile = Profile()
        user_profile.user = new_user
        user_profile.save()
        return user_profile
