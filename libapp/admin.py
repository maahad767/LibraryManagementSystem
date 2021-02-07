from django.contrib import admin

from . import models


class CopyInline(admin.TabularInline):
    model = models.Copy


class BookAdmin(admin.ModelAdmin):
    inlines = [
        CopyInline,
    ]
    autocomplete_fields = ['category']


class AuthorAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']


class PublisherAdmin(admin.ModelAdmin):
    pass


class BookSaleAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.Book, BookAdmin)
admin.site.register(models.BookSaleRecord, BookSaleAdmin)

