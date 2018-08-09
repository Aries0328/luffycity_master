from api import models
from django.shortcuts import HttpResponse
from api.serializers.course import CourseSeriailzer
from api.serializers.course import DegreeCourseSerializer
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api.serializers import serializers
from api.utils import response
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

class Course(ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = CourseSeriailzer


class DegreeCourse(ModelViewSet):
    queryset = models.DegreeCourse.objects.all()
    serializer_class = DegreeCourseSerializer

class CoursesView(APIView):
    def get(self, request, *args, **kwargs):
        result = ""
        if request.version == "v1":
            result = "v1"
        else:
            result = "其它"
        return HttpResponse(result)

class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = course.CourseSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)

# a.查看所有学位课并打印学位课名称以及授课老师
class AllDcourseTeacher(APIView):
    def get(self, request, *args, **kwargs):
        ret = response.BaseResponse()
        queryset = models.DegreeCourse.objects.all()
        print(queryset)
        page = PageNumberPagination()
        print(page)
        course_list = page.paginate_queryset(queryset, request, self)
        print(course_list)
        ser = serializers.DegreecourseTeacherSerializer(instance=course_list, many=True)
        ret.data = ser.data
        return Response(ret.dict)


# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class AllDegreecourseScholarship(APIView):
    def get(self, request, *args, **kwargs):
        ret = response.BaseResponse()
        queryset = models.DegreeCourse.objects.all()
        ser = serializers.DegreecourseScholarshipSerializer(instance=queryset, many=True)
        ret.data = ser.data
        return Response(ret.dict)


# c.展示所有的专题课
class AllCourse(APIView):
    def get(self, request, *args, **kwargs):
        ret = response.BaseResponse()
        queryset = models.Course.objects.filter(degree_course__isnull=True)
        ser = serializers.AllCourseSerializer(instance=queryset, many=True)
        ret.data = ser.data
        return Response(ret.data)


# d. 查看id=1的学位课对应的所有模块名称
class DegreecourseModule(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = response.BaseResponse()
        queryset = models.DegreeCourse.objects.get(pk=pk)
        ser = serializers.DegreecourseModuleSerializer(instance=queryset)
        print(type(ser.data))
        ret.data = ser.data
        return Response(ret.dict)


#  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseDetail(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = response.BaseResponse()
        queryset = models.Course.objects.get(pk=pk)
        ser = serializers.CourseDetailSerializer(instance=queryset)
        ret.data = ser.data
        return Response(ret.dict)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuestion(APIView):
    def get(self, request, pk, *args, **kwargs):
        res = response.BaseResponse()
        queryset = models.Course.objects.get(pk=pk)
        ser = serializers.CourseQASerializer(instance=queryset)
        res.data = ser.data
        return Response(res.dict)


# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseOutline(APIView):
    def get(self, request, pk, *args, **kwargs):
        res = response.BaseResponse()
        queryset = models.Course.objects.get(pk=pk)
        ser = serializers.CourseOutlineSerializer(instance=queryset)
        res.data = ser.data
        return Response(res.dict)


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseChapter(APIView):
    def get(self, request, pk, *args, **kwargs):
        res = response.BaseResponse()
        queryset = models.Course.objects.get(pk=pk)
        ser = serializers.CourseChapterSerializer(instance=queryset)
        res.data = ser.data
        return Response(res.dict)


