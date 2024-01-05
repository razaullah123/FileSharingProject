from django.contrib import admin
from django.urls import path, include

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('file_sharing.urls')),
    # path('api/token/', get_tokens_for_user, name='get_tokens_for_user'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
