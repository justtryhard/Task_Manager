from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('work/', include('work.urls')),
    # path('login/', views.login, name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='main/logged_out.html'), name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]