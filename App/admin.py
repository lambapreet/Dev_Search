from django.contrib import admin
from .models import ProjectModel, ReviewModel

# Register your models here.

admin.site.register(ProjectModel)
admin.site.register(ReviewModel)