from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from snippets import views

app_name = "snippets"

schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url('schema', schema_view),
    url('', include(router.urls)),
]