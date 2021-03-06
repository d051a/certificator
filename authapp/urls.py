from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    # Examples:
    # url(r'^$', '_WEBPRINT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^registration/$', views.RegisterFormView.as_view(), name='registration'),
    url(r'^login/$', views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
