from django.contrib import admin

from retail_network.models import Contacts, Link, Product


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "debt",
        "provider",
    )
    list_display_links = ("provider",)
    list_filter = (
        "contacts__city",
        "provider",
    )
    search_fields = ("name",)
    actions = ("clear_debt",)

    @admin.action(description="Clear debt for selected links")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0.0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    list_filter = (
        "name",
        "release_date",
    )
    search_fields = ("name",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "link")
    list_filter = (
        "country",
        "city",
    )
