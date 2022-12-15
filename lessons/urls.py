from django.urls import path

from . import views
from .views import CreateProducts, CreateChapter, CreateLessons, CreateComment

app_name = "lessons"


urlpatterns = [
    path("", views.ProductListView.as_view(), name="home"),
    path("cat/", views.CategoryListView.as_view(), name="category"),
    path("comm/", views.CommentListView.as_view(), name="category"),
    # path("subcat/", views.SubCategoryListView.as_view(), name="subcategory"),
    path("lessonsCat/", views.ChapterListView.as_view(), name="chapter"),
    path("lessons/", views.LessonsListView.as_view(), name="lessons"),
    path("detail/<int:pk>/", views.DetailProducts.as_view(), name="detail"),
    path('createP/', CreateProducts.as_view(), name="createP"),
    path('createC/', CreateChapter.as_view(), name="createC"),
    path('createL/', CreateLessons.as_view(), name="createL"),
    path('commentC/', CreateComment.as_view(), name="CommentCreate"),

]

