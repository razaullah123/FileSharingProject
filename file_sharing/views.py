from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import authenticate
from django.db.models import Q

from file_sharing.models import Group, File, User
from .serializers import (GroupSerializer, MediaSerializer, UserRegisterSerializer,
                          UserSerializer, MediaReadSerializer, GroupReadSerializer)


class UserSignUpView(generics.CreateAPIView, generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer_registration = self.serializer_class(data=request.data)
        if not serializer_registration.is_valid():
            return Response({'result': serializer_registration.errors})
        user = serializer_registration.save()
        serialized_data = UserRegisterSerializer(user).data
        return Response({"result": "User Register Successfully", "data": serialized_data})


class UserLoginView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer_login = self.serializer_class(data=request.data)
        if not serializer_login.is_valid():
            return Response({'result': serializer_login.errors})
        user = authenticate(username=request.data.get(
            "username"), password=request.data.get("password"))
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
            })
        else:
            return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GroupReadView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupReadSerializer
    permission_classes = [IsAuthenticated]


class MediaUploadView(generics.CreateAPIView):
    queryset = File.objects.all()
    serializer_class = MediaSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        request.data["uploaded_by"] = request.user.id
        return super().create(request, *args, **kwargs)


class MediaListView(generics.ListAPIView):
    queryset = File.objects.all()
    serializer_class = MediaReadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return File.objects.filter(
            Q(uploaded_by=user) | (Q(is_private=False) & Q(group__members=user))
        ).distinct()
