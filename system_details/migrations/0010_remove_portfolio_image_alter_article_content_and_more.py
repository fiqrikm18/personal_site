# Generated by Django 5.1.3 on 2025-03-25 05:38

import ckeditor.fields
import django.db.models.deletion
import system_details.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_details', '0009_skillset_year_experience'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='image',
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='description',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=system_details.models.case_upload_location)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_details.portfolio')),
            ],
            options={
                'db_table': 'portfolio_images',
            },
        ),
    ]
