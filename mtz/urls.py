
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accountsL/',include('accounts.urls')),
    path('card/',include('pageCard.urls'),),
    path("cart/",include("cart.urls")),
    path("staff/",include("staffPage.urls")),
    ] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

