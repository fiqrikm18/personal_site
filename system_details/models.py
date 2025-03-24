from django.db import models
from libs.models import base_model

SKILL_LEVEL = (
    ('BASIC', 'Basic'),
    ('INTERMEDIATE', 'Intermediate'),
    ('EXPERT', 'Expert')
)


# Create your models here.
class WorkingExperience(base_model.BaseModel):
    role = models.CharField()
    company = models.CharField()
    region = models.CharField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, default=None, blank=True)

    class Meta:
        db_table = 'working_experiences'


class SkillSet(base_model.BaseModel):
    name = models.CharField()
    level = models.CharField(choices=SKILL_LEVEL)
    image = models.ImageField(null=True)

    class Meta:
        db_table = 'skill_sets'


class Portfolio(base_model.BaseModel):
    title = models.CharField()
    company = models.CharField()
    year = models.DateField()
    description = models.TextField()
    image = models.ImageField(null=True)

    class Meta:
        db_table = 'portfolios'


class Article(base_model.BaseModel):
    title = models.CharField()
    slug = models.CharField()
    content = models.TextField()
    image = models.ImageField(null=True)

    class Meta:
        db_table = 'articles'


class Testimony(base_model.BaseModel):
    text = models.CharField()
    author = models.CharField(max_length=50)
    roles = models.CharField()
    company = models.CharField()

    class Meta:
        db_table = 'testimonies'
