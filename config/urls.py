from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from config.views import home_page, login_view, register_view, profile_view

app_name = 'book'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('user/', include("apps.users.urls")),
    path('books/', include("apps.books.urls")),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
