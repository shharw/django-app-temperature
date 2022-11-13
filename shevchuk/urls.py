from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.views.generic.base import RedirectView


urlpatterns = [    
    path('temperature/', include('temperature.urls')),
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='temperature/')),
    path('', include('social_django.urls', namespace='social')),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
