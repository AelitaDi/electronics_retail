from django.core.validators import MinValueValidator
from django.db import models

NULLABLE = {"blank": True, "null": True}


class Product(models.Model):
    """
    Модель продукта.
    """

    name = models.CharField(
        max_length=250,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    model = models.CharField(
        max_length=250,
        verbose_name="Модель",
        help_text="Введите модель продукта",
    )
    release_date = models.DateField(
        verbose_name="Дата выхода продукта на рынок",
        help_text="Введите дату выхода продукта на рынок",
    )

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ["name", "release_date"]


class Link(models.Model):
    """
    Модель звена сети.
    """

    name = models.CharField(
        max_length=250,
        verbose_name="Наименование",
        help_text="Введите наименование звена",
    )
    products = models.ManyToManyField(
        "Product", related_name="products", verbose_name="продукты"
    )
    provider = models.ForeignKey(
        "Link",
        on_delete=models.SET_NULL,
        verbose_name="поставщик",
        help_text="Укажите поставщика",
        **NULLABLE,
    )
    debt = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0)],
        verbose_name="задолженность перед поставщиком",
        help_text="Укажите величину задолженности",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "звено"
        verbose_name_plural = "звенья"
        ordering = ["name", "debt"]


class Contacts(models.Model):
    """
    Модель контактов звена сети.
    """

    link = models.ForeignKey(
        "Link", on_delete=models.CASCADE, verbose_name="Звено", related_name="contacts"
    )
    email = models.EmailField(
        verbose_name="Email", help_text="Введите Email", **NULLABLE
    )
    country = models.CharField(
        max_length=150,
        verbose_name="Страна",
        help_text="Введите страну",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=150,
        verbose_name="Город",
        help_text="Введите город",
        **NULLABLE,
    )
    street = models.CharField(
        max_length=150,
        verbose_name="Улица",
        help_text="Введите улицу",
        **NULLABLE,
    )
    house_number = models.CharField(
        max_length=150,
        verbose_name="Номер дома",
        help_text="Введите номер дома",
        **NULLABLE,
    )

    def __str__(self):
        return f"{self.email} {self.link.name}"

    class Meta:
        verbose_name = "контакты"
        verbose_name_plural = "контакты"
