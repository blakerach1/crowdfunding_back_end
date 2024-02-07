from django.db import models
from django.contrib.auth import get_user_model


class Categories(models.Model):
    CATEGORY_CHOICES = [
        ('Stewardship', 'Stewardship'),
        ('Education Access', 'Education Access'),
        ('Health and Wellness', 'Health and Wellness'),
        ('Innovation for Social Impact', 'Innovation for Social Impact'),
        ('Sustainable Development', 'Sustainable Development'),
        ('Crisis Response and Relief', 'Crisis Response and Relief'),
        ('Tech for Good', 'Tech for Good'),
        ('Animal Welfare', 'Animal Welfare'),
        ('Clean Energy Initiatives', 'Clean Energy Initiatives'),
        ('Food Security', 'Food Security'),
        ('Mental Health Support', 'Mental Health Support'),
        ('Community Resilience', 'Community Resilience'),
    ]

    title = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

    description = models.CharField(max_length=500)

    class Meta:
        ordering = ["title"]    
    
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
        )
    category = models.ManyToManyField(Categories, related_name='projects')

    def __str__(self):
        return self.title


class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    pledge_date = models.DateTimeField(auto_now=True)
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

