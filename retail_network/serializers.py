from rest_framework import serializers

from retail_network.models import Contacts, Link, Product
from retail_network.validators import DebtValidator


class ProductSerializer(serializers.ModelSerializer):
    """
    Сериализатор для продуктов.
    """

    class Meta:
        model = Product
        fields = [
            "name",
            "model",
        ]


class ContactsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для контактов.
    """

    class Meta:
        model = Contacts
        fields = [
            "country",
            "city",
        ]


class LinkSerializer(serializers.ModelSerializer):
    """
    Сериализатор для звеньев сети.
    """

    products = ProductSerializer(read_only=True, many=True)
    contacts = ContactsSerializer(read_only=True, many=True)

    class Meta:
        model = Link
        fields = (
            "name",
            "products",
            "provider",
            "debt",
            "created_at",
            "contacts",
        )
        validators = [
            DebtValidator("provider", "debt"),
        ]


class LinkListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка звеньев сети.
    """

    class Meta:
        model = Link
        fields = (
            "name",
            "provider",
            "debt",
            "created_at",
        )


class LinkUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для обновления звеньев сети.
    """

    class Meta:
        model = Link
        fields = (
            "name",
            "products",
            "created_at",
        )
