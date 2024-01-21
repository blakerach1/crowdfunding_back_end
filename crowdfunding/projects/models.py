from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
        )

    def __str__(self):
        return self.title


# The related name specifies the name of the reverse relationship 

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='pledges'
    )


class Category(models.Model):
    PROJECT_CATEGORY_CHOICES = [
        ("COE", "Community Empowerment"),
        ("ENS", "Environmental Stewardship"),
        ("EDA", "Education Access"),
        ("HEW", "Health and Wellness"),
        ("EQI", "Equity and Inclusion"),
        ("INS", "Innovation for Social Impact"),
        ("SUD", "Sustainable Development"),
        ("CRR", "Crisis Response and Relief"),
        ("TEG", "Tech for Good"),
        ("ANW", "Animal Welfare"),
        ("CEI", "Clean Energy Initiatives"),
        ("FOS", "Food Security"),
        ("COR", "Community Resilience"),
        ]

    title = models.CharField(max_length=200, choices=PROJECT_CATEGORY_CHOICES)
    description = models.CharField(max_length=200)
    # thumbnail = models.FileField(upload_to=settings.STATIC_ROOT, null=True, blank=True, storage=settings.THUMBNAIL_STORAGE),
    project = models.ManyToManyField('Project')


    class Meta:
        ordering = ["title"]
    
    
    def __str__(self):
        return f'{self.get_title_display()}'
