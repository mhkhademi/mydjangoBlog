from django.contrib import admin
from . import models

@admin.action(description='Mark selected articles as released')
def all_released(modeladmin, request, queryset):
    queryset.update(release_status=True)

@admin.action(description='Mark selected articles as not released')
def all_not_released(modeladmin, request, queryset):
    queryset.update(release_status=False)


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ('title','category__categoryname','author__username','release_status')
    ordering = ('date',)
    list_display = ('title','author','date','category','release_status')
    list_display_links = ('title',)
    actions = [all_released,all_not_released]
    list_filter = ('category__categoryname','author__username','release_status')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('categoryname',)
    ordering = ('date',)
    list_display = ('categoryname','author','date')
    list_display_links = ('categoryname',)
    list_filter = ('author__username',)
