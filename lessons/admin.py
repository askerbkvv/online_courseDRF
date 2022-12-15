from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import (
    Category,
    SubCategory,
    Product,
    LessonsCat,
    Lessons,
    Comment, Include
)

admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)
admin.site.register(LessonsCat)
admin.site.register(Lessons)
admin.site.register(Comment)
admin.site.register(Include)


