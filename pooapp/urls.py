from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.poops import PoopsViewSet, poop_evaluation

router = DefaultRouter()
router.register(r'poops', PoopsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('evaluate-poop/<int:user_id>/', poop_evaluation, name='evaluate-poop')
]
