from rest_framework import serializers
from api.models import *


class CourseModelSerialize(serializers.ModelSerializer):
    level = serializers.CharField(source='get_level_display')  # level字段变中文

    class Meta:
        model = Course
        fields = ['id', 'name', 'level', 'course_img', 'sub_category', 'course_type', 'degree_course', 'brief', 'pub_date', 'period', 'order', 'attachment_path', 'status', 'template_id']


class CourseDetailModelSerialize(serializers.ModelSerializer):
    name = serializers.CharField(source='course.name')
    img = serializers.CharField(source='course.course_img')
    level = serializers.CharField(source='course.get_level_display')
    #
    # # m2m
    recommends = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    class Meta:
        model = CourseDetail
        # fields = ['name', 'img', 'level', 'recommends', 'chapter']
        fields = ['name', 'img', 'level', 'course_slogan', 'why_study', 'recommends', 'chapter', 'hours', 'video_brief_link', 'what_to_study_brief', 'career_improvement', 'prerequisite', 'teachers']
        # depth = 1

    def get_recommends(self, obj):  # obj为model中的Course类
        queryset = obj.recommend_courses.all()
        return [{'id': c.pk, 'course': c.name} for c in queryset]  # 取出多对多字段的值

    def get_chapter(self, obj):
        queryset = obj.course.coursechapter_set.all()
        return [{'id': c.pk, 'num': c.chapter, 'chapter': c.name} for c in queryset]

    def get_teachers(self, obj):
        queryset = obj.teachers.all()
        return [{'id': c.pk, 'teacher': c.name} for c in queryset]

