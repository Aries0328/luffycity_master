from api import models
from rest_framework import serializers

class CourseSeriailzer(serializers.ModelSerializer):
    course_type = serializers.CharField(source="get_course_type_display")
    level = serializers.CharField(source='get_level_display')
    status = serializers.CharField(source="get_status_display")
    class Meta:
        model = models.Course
        fields = "__all__"
        depth = 2


class DegreeCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DegreeCourse
        fields = "__all__"
        depth = 2


class TeacherSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="get_role_display")
    class Meta:
        model = models.Teacher
        fields = "__all__"