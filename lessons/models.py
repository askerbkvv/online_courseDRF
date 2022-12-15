
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from users.models import User

LANGUAGES = (
    ('EN', 'english'),
    ('RUS', 'russian'),
    ('KGZ', 'kyrgyz')
)


class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    slug = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class SubCategory(models.Model):
    name = models.CharField("Подкатегории", max_length=100)
    slug = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='sub_categories', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "SubCategory"
        verbose_name_plural = "SubCategories"


class Include(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Include"
        verbose_name_plural = "Includes"


class Product(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField("Краткое описание", max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    time_update = models.DateTimeField(auto_now=True)
    language = models.CharField(max_length=30, choices=LANGUAGES, default='russian')
    description = models.TextField("Описание")
    price = models.DecimalField('Цена', max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    subcategory = ChainedForeignKey(
        SubCategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    include = models.ManyToManyField(Include)
    slug = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class LessonsCat(models.Model):
    title = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lesson_categories', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Chapter"
        verbose_name_plural = "Chapters"


class Lessons(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to="lessons_video", null=True)
    lesson_category = models.ForeignKey(LessonsCat, on_delete=models.CASCADE, related_name='lessons', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, related_name='comments', null=True)
    content = models.TextField()

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"



