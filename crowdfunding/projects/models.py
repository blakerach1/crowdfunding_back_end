from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=500)

    class Meta:
        ordering = ["title"]    
    
    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/placeholder-image.png')
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='owned_projects'
        )
    categories = models.ManyToManyField(Category, related_name='projects')

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

