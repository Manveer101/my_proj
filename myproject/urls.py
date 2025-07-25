from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from blog.views import BlogViewSet
from rest_framework.routers import DefaultRouter
from myapp.views import LoginView, SignupView, SecretView, ChangePasswordView, PasswordResetRequestView, PasswordResetConfirmView
from rest_framework.authtoken.views import obtain_auth_token
from myapp.views import MyProtectedView

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/signup/', SignupView.as_view(), name='signup'),
    path('api/login/', LoginView.as_view(), name='api-login'),
    path('api/secret/', SecretView.as_view(), name='secret'),
    path('reset-password/', auth_views.PasswordResetView.as_view(), name='reset-password'),
    path('reset-password-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('api-token-auth/', obtain_auth_token),
    path('protected/',MyProtectedView.as_view(), name='protected-view'),
    
]


urlpatterns += [
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
]

urlpatterns += [
    path('reset-password-request/', PasswordResetRequestView.as_view(), name='reset-password-request'),
    path('reset-password-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='reset-password-confirm'),
]


from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
