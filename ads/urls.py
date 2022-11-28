from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads.views import LocationViewSet, CategoryViewSet, AdViewSet, index, UserViewSet, SelectionListView, \
    SelectionDetailView, AdCreateView, AdUpdateView, AdDetailView

router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'cat', CategoryViewSet)
router.register(r'user', UserViewSet)
router.register(r'ad', AdViewSet)


urlpatterns = [
    path("", index),

    path('login/', views.obtain_auth_token),
    # path('logout/', Logout.as_view()),
    path("", include(router.urls)),

    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view()),
    path('ad/create/', AdCreateView.as_view()),
    path('ad/<int:pk>/update/', AdUpdateView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('selection/', SelectionListView.as_view()),
    path('selection/<int:pk>/', SelectionDetailView.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
