from rest_framework.routers import DefaultRouter
from .viewsets import CadastroViewSet

router = DefaultRouter()

router.register('cadastro', CadastroViewSet)


urlpatterns = router.urls