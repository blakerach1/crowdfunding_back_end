# Generated by Django 4.2.3 on 2024-01-27 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_alter_categories_description_alter_categories_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='title',
            field=models.CharField(choices=[('Crisis Response and Relief', 'Crisis Response and Relief'), ('Community Resilience', 'Community Resilience'), ('Environmental Stewardship', 'Environmental Stewardship'), ('Equity and Inclusion', 'Equity and Inclusion'), ('Community Empowerment', 'Community Empowerment'), ('Animal Welfare', 'Animal Welfare'), ('Education Access', 'Education Access'), ('Health and Wellness', 'Health and Wellness'), ('Tech for Good', 'Tech for Good'), ('Clean Energy Initiatives', 'Clean Energy Initiatives'), ('Innovation for Social Impact', 'Innovation for Social Impact'), ('Sustainable Development', 'Sustainable Development'), ('Food Security', 'Food Security')], max_length=200),
        ),
    ]
