from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #  Include helps with pointing out the root of URLconf on the
    # polls.urls module.
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]