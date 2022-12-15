from rest_framework import generics, mixins
from lessons.models import Product, Category, SubCategory, LessonsCat, Lessons, Comment
from lessons.serializers import ProductSerializer, CategorySerializer, SubCategorySerializer, \
    LessonsSerializer, DetailSerializer, ChapterSerializer, CommentSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryListView(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ChapterListView(generics.ListAPIView):
    queryset = LessonsCat.objects.all()
    serializer_class = ChapterSerializer


class LessonsListView(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class CommentListView(generics.ListAPIView):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer


class DetailProducts(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    generics.RetrieveAPIView,
    mixins.ListModelMixin
):
    # permission_classes = [RolePermissions]
    queryset = Product.objects.all()
    serializer_class = DetailSerializer

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CreateProducts(mixins.CreateModelMixin, generics.ListAPIView):
    # permission_classes = [RolePermissions]
    serializer_class = ProductSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Product.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class CreateChapter(mixins.CreateModelMixin, generics.ListAPIView):
    # permission_classes = [RolePermissions]
    serializer_class = ChapterSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = LessonsCat.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class CreateLessons(mixins.CreateModelMixin, generics.ListAPIView):
    # permission_classes = [RolePermissions]
    serializer_class = LessonsSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Lessons.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class CreateComment(mixins.CreateModelMixin, generics.ListAPIView):
    # permission_classes = [RolePermissions]
    serializer_class = CommentSerializer
    passed_id = None

    def get_queryset(self):
        request = self.request
        qs = Comment.objects.all()
        query = request.GET.get('q')
        if query is not None:
            qs = qs.filter(content__icontains=query)
        return qs

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)