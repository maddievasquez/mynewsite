from django.contrib import admin

# We can find all models that handle the superuser settings.
# In order to make the admin modifiable we need to we need to tell the admin
# that Question objects have an admin interface. This will allow us to change/add new
# questions through the admin interface
from .models import Question

admin.site.register(Question)
