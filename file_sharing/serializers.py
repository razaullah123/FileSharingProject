from rest_framework import serializers

from file_sharing.models import User, Group, File


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.CharField()
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "username",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class GroupReadSerializer(serializers.ModelSerializer):
    creator = UserRegisterSerializer()
    members = UserRegisterSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {"creator": {"required": False}}


class GroupSerializer(serializers.ModelSerializer):
    # creator = UserRegisterSerializer()
    # members = UserRegisterSerializer(many=True)

    class Meta:
        model = Group
        fields = '__all__'
        extra_kwargs = {"creator": {"required": False}}


class MediaSerializer(serializers.ModelSerializer):
    # uploaded_by = UserRegisterSerializer()
    # group = GroupSerializer()

    class Meta:
        model = File
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "username",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    email = serializers.CharField(label=("email"), write_only=True)
    username = serializers.CharField(label=("usernmae"), write_only=True)
    password = serializers.CharField(
        label=("password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )

    class Meta:
        model = User


class MediaReadSerializer(serializers.ModelSerializer):
    uploaded_by = UserRegisterSerializer()
    group = GroupReadSerializer()

    class Meta:
        model = File
        fields = '__all__'
