from django.urls import path
from .views import (UserSignUpView, UserLoginView, GroupCreateView,
                    MediaUploadView, MediaListView, GroupReadView)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('create-group/', GroupCreateView.as_view(), name='create-group'),
    path('read-group/', GroupReadView.as_view(), name="read-group"),
    path('upload-media/', MediaUploadView.as_view(), name='upload-media'),
    path('list-media/', MediaListView.as_view(), name='list-media'),
]
