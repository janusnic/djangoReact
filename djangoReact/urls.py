from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers, serializers, viewsets
from djangoReact.apps.comments.views import CommentViewSet
from djangoReact.apps.users.models import User

admin.autodiscover()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_satff')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = patterns(
    '',
    url(
        r'^$',
        TemplateView.as_view(template_name='base.html'),
        name='homepage'
    ),
    url(
        r'^api/',
        include(router.urls)
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^/app/', include('apps.app.urls', namespace='app')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url("^404/$", TemplateView.as_view(template_name="404.html")),
        url("^500/$", TemplateView.as_view(template_name="500.html")),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
