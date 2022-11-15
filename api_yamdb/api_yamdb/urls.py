from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    path('api/v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('api/v1/', include('djoser.urls.jwt')),

]
