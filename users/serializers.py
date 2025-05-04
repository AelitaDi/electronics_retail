from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    """
    Сериализатор для просмотра общей информации о пользователях.
    """

    class Meta:
        model = User
        fields = (
            "email",
            "is_active",
            "is_staff",
            "id",
        )


class UserSelfSerializer(ModelSerializer):
    """
    Сериализатор для создания, редактирования и просмотра собственного профиля.
    """

    class Meta:
        model = User
        fields = "__all__"
