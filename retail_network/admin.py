from django.contrib import admin

from retail_network.models import Link, Product, Contacts


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "debt", "provider",)
    list_filter = ("contacts__city", "provider",)
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "model", "release_date")
    list_filter = ("name", "release_date",)
    search_fields = ("name",)


@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ("email", "country", "city", "link")
    list_filter = ("country", "city",)
