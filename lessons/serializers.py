from rest_framework import serializers

from .models import Category, Product, SubCategory, LessonsCat, Lessons, Comment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['sub_categories'] = SubCategorySerializer(instance.sub_categories.all(), many=True).data
        return representation


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonsCat
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['lesson'] = LessonsSerializer(instance.lessons.all(), many=True).data
        return representation


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(instance.lesson_categories.all())
        representation['lesson_categories'] = ChapterSerializer(instance.lesson_categories.all(), many=True).data
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data
        return representation


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"

