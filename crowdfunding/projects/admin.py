from django.contrib import admin
from .models import Project, Pledge, Categories
from users.models import CustomUser

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)


class PledgeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pledge, PledgeAdmin)


class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(CustomUser, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Categories, ProjectAdmin)