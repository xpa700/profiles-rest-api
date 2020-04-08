from django.contrib import admin
from profiles_api import models

# Register your models here.
# We have to register them so they can be visible
# and manageable on the Django web admin page
admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
