from django.contrib import admin
from site_app.models import Group, Category, Series, Product, Variable


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(Variable)
class VariableAdmin(admin.ModelAdmin):
    list_filter = ('product',)
