from django.contrib import admin
from django.utils.html import format_html
from .models import (
    WorkingExperience,
    SkillSet,
    Portfolio,
    Article,
    Testimony,
    PortfolioImages,
)


# Register your models here.
class WorkingExperienceAdmin(admin.ModelAdmin):
    list_display = [
        "role",
        "company",
        "region",
        "start_date",
        "end_date",
    ]

    search_fields = ["role"]


class SkillSetsAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "level",
        "image",
    ]

    search_fields = ["name"]

    def image_tag(self, obj):
        return format_html('<img style="width:50px;" src="{}" />'.format(obj.image.url))

    image_tag.short_description = "Image"


class PortfolioImageAdmin(admin.StackedInline):
    model = PortfolioImages


class PortfolioAdmin(admin.ModelAdmin):
    inlines = [PortfolioImageAdmin]
    list_display = [
        "title",
    ]


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "image", "summary_content"]

    def summary_content(self, obj):
        return obj.content[:50]


class TestimonyAdmin(admin.ModelAdmin):
    pass


admin.site.register(WorkingExperience, WorkingExperienceAdmin)
admin.site.register(SkillSet, SkillSetsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Testimony, TestimonyAdmin)
