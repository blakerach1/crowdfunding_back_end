# Generated by Django 4.2.3 on 2024-01-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_remove_project_category_category_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(choices=[('Animal Welfare', 'Animal Welfare'), ('Food Security', 'Food Security'), ('Education Access', 'Education Access'), ('Community Resilience', 'Community Resilience'), ('Sustainable Development', 'Sustainable Development'), ('Tech for Good', 'Tech for Good'), ('Health and Wellness', 'Health and Wellness'), ('Community Empowerment', 'Community Empowerment'), ('Environmental Stewardship', 'Environmental Stewardship'), ('Crisis Response and Relief', 'Crisis Response and Relief'), ('Clean Energy Initiatives', 'Clean Energy Initiatives'), ('Innovation for Social Impact', 'Innovation for Social Impact'), ('Equity and Inclusion', 'Equity and Inclusion')], max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('project', models.ManyToManyField(related_name='categories', to='projects.project')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
