from django.contrib import admin
from .models import WorkingExperience, SkillSet, Portfolio, Article, Testimony


# Register your models here.
class WorkingExperienceAdmin(admin.ModelAdmin):
    list_display = [
        'role',
        'company',
        'region',
        'start_date',
        'end_date',
    ]

    search_fields = ['role']

class SkillSetsAdmin(admin.ModelAdmin):
    pass


class PortfolioAdmin(admin.ModelAdmin):
    pass


class ArticleAdmin(admin.ModelAdmin):
    pass


class TestimonyAdmin(admin.ModelAdmin):
    pass


admin.site.register(WorkingExperience, WorkingExperienceAdmin)
admin.site.register(SkillSet, SkillSetsAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Testimony, TestimonyAdmin)
