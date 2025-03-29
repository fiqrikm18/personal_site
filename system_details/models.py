from django.db import models
from libs.models import base_model
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.widgets import CKEditorUploadingWidget

SKILL_LEVEL = (
    ("BASIC", "Basic"),
    ("INTERMEDIATE", "Intermediate"),
    ("EXPERT", "Expert"),
)

def case_upload_location(instance, filename):
    file_name = filename.lower().replace(" ", "-")
    return "{}".format( file_name)


# Create your models here.
class WorkingExperience(base_model.BaseModel):
    role = models.CharField()
    company = models.CharField()
    region = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, default=None, blank=True)

    class Meta:
        db_table = "working_experiences"


class SkillSet(base_model.BaseModel):
    name = models.CharField()
    level = models.CharField(choices=SKILL_LEVEL)
    image = models.ImageField(null=True)
    year_experience = models.IntegerField(default=0)

    class Meta:
        db_table = "skill_sets"


class Portfolio(base_model.BaseModel):
    title = models.CharField()
    company = models.CharField()
    year = models.DateField()
    url = models.CharField(null=True, blank=True)
    summary = models.CharField(null=True, blank=True)
    description = RichTextField(null=True)

    class Meta:
        db_table = "portfolios"
        
class PortfolioImages(base_model.BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    file = models.FileField(upload_to=case_upload_location, null = True, blank = True)
    
    class Meta:
        db_table = "portfolio_images"
    


class Article(base_model.BaseModel):
    title = models.CharField()
    slug = models.CharField()
    image = models.ImageField(null=True)
    content = RichTextField(null=True)

    class Meta:
        db_table = "articles"

    def save(self, *args, **kwargs):
        if not self.slug:
            potential_slug = slugify(self.title)
            if Article.objects.filter(slug=potential_slug).exists():
                i = 1
                while Article.objects.filter(
                    slug=potential_slug + "-" + str(i)
                ).exists():
                    i += 1
                self.slug = potential_slug + "-" + str(i)
            else:
                self.slug = potential_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Testimony(base_model.BaseModel):
    text = models.CharField()
    author = models.CharField(max_length=50)
    roles = models.CharField()
    company = models.CharField()

    class Meta:
        db_table = "testimonies"
