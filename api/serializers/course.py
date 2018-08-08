# from rest_framework import serializers
# from api import models
#
# class CourseSeriailzer(serializers.ModelSerializer):
#     course_type = serializers.CharField(source="get_course_type_display")
#     level = serializers.CharField(source='get_level_display')
#     status = serializers.CharField(source="get_status_display")
#     class Meta:
#         model = models.Course
#         fields = "__all__"
#         depth = 2
#
#
# class DegreeCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DegreeCourse
#         fields = "__all__"
#         depth = 2
#
#
# class TeacherSerializer(serializers.ModelSerializer):
#     role = serializers.CharField(source="get_role_display")
#     class Meta:
#         model = models.Teacher
#         fields = "__all__"
#
#
# # a.查看所有学位课并打印学位课名称以及授课老师
# class DegreecourseTeachersSerializer(serializers.ModelSerializer):
#     teacherName = serializers.SerializerMethodField()
#
#     def get_teacherName(self, obj):
#         return [item.name for item in obj.teachers.all()]
#
#     class Meta:
#         model = models.DegreeCourse
#         fields = ["name", "teacherName"]
#
#
# # b.查看所有学位课并打印学位课名称以及学位课的奖学金
# class DegreecourseScholarshipSerializer(serializers.ModelSerializer):
#     scholarship = serializers.SerializerMethodField()
#
#     def get_scholarship(self, obj):
#         return [(item.time_percent, item.value) for item in obj.scholarship_set.all()]
#
#     class Meta:
#         model = models.DegreeCourse
#         fields = ["name", "scholarship"]
#
#
# # c.展示所有的专题课
# class AllCourseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Course
#         fields = "__all__"
#
#
# # d. 查看id=1的学位课对应的所有模块名称
# class DegreecourseModuleSerializer(serializers.ModelSerializer):
#     moduleName = serializers.SerializerMethodField()
#
#     def get_moduleName(self, obj):
#         return [item.name for item in obj.course_set.all()]
#
#     class Meta:
#         model = models.DegreeCourse
#         fields = ["name", "moduleName"]
#
#
# #  e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
# class CourseDetailSerializer(serializers.ModelSerializer):
#     level = serializers.CharField(source="get_level_display")
#     why_study = serializers.CharField(source="coursedetail.why_study")
#     what_to_study_brief = serializers.CharField(source="coursedetail.what_to_study_brief")
#     recommend_courses = serializers.SerializerMethodField()
#
#     def get_recommend_courses(self, obj):
#         return [item.name for item in obj.coursedetail.recommend_courses.all()]
#
#     class Meta:
#         model = models.Course
#         fields = ["name", "level", "why_study", "what_to_study_brief", "recommend_courses"]
#
#
# # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
# class CourseQuestionSerializer(serializers.ModelSerializer):
#     QuestionList = serializers.SerializerMethodField()
#
#     def get_QuestionList(self0, obj):
#         return [(item.question, item.answer) for item in obj.asked_question.all()]
#
#     class Meta:
#         model = models.Course
#         fields = ["name", "QuestionList"]
#
#
# # g.获取id = 1的专题课，并打印该课程相关的课程大纲
# class CourseOutlineSerializer(serializers.ModelSerializer):
#     outline = serializers.SerializerMethodField()
#
#     def get_outline(self, obj):
#         return [(item.title, item.content) for item in obj.coursedetail.courseoutline_set.all()]
#
#     class Meta:
#         model = models.Course
#         fields = ["name", "outline",]
#
#
# # h.获取id = 1的专题课，并打印该课程相关的所有章节
# class CourseChapterSerializer(serializers.ModelSerializer):
#     chapter = serializers.SerializerMethodField()
#     def get_chapter(self, obj):
#         return [{"chapter":item.chapter, "name": item.name, "summary":item.summary, "pubdate":item.pub_date} for item in obj.coursechapters.all()]
#     class Meta:
#         model = models.Course
#         fields = ["name", "chapter"]



from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    course_img = serializers.CharField()
    sub_category = serializers.SerializerMethodField()
    course_type = serializers.CharField(source='get_course_type_display')
    degree_course = serializers.SerializerMethodField()
    brief = serializers.CharField()
    level = serializers.CharField(source='get_level_display')
    pub_date = serializers.DateField()
    period = serializers.IntegerField()  #
    order = serializers.IntegerField()
    attachment_path = serializers.CharField()
    status = serializers.CharField(source='get_status_display')
    template_id = serializers.IntegerField()

    def get_sub_category(self,obj):
        category_dic = {'id':obj.sub_category.id,'name':obj.sub_category.name}
        return category_dic


    def get_degree_course(self,obj):
        degree_dic = {}
        if obj.degree_course is not None:
            degree_dic = {'id':obj.degree_course.id,'name':obj.degree_course.name}
        return degree_dic

class CourseModelSerializer(CourseSerializer):

    course_detail = serializers.SerializerMethodField()
    chapter = serializers.SerializerMethodField()
    askedquestion = serializers.SerializerMethodField()

    def get_course_detail(self,obj):
        '''
        获取模块详情对象
        :param ojb:
        :return:
        '''
        course_obj = {'why_study':obj.coursedetail.why_study,'what_to_study_brief':obj.coursedetail.what_to_study_brief,'recommend_courses':[]}
        for i in obj.coursedetail.recommend_courses.all():
            course_obj['recommend_courses'].append(i.name)
        return course_obj

    def get_chapter(self,obj):
        '''
        获取章节对象
        :param obj:
        :return:
        '''
        chapter_obj = obj.coursechapters.all().values('chapter','name','summary')
        return chapter_obj

    def get_askedquestion(self,obj):
        '''
        通过contentType表获取asked表对象
        :param obj:
        :return:
        '''
        question_obj = obj.asked_question.all().values('question','answer')
        return question_obj

class TeacherSerializer(serializers.Serializer):
    name = serializers.CharField()
    role = serializers.CharField(source='get_role_display')
    title = serializers.CharField()
    signature = serializers.CharField()
    image = serializers.CharField()
    brief = serializers.CharField()

class DegreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    course_img = serializers.CharField()
    brief = serializers.CharField()
    total_scholarship = serializers.IntegerField()
    mentor_compensation_bonus = serializers.IntegerField()
    period = serializers.IntegerField()
    prerequisite = serializers.CharField()
    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()
    model_name = serializers.SerializerMethodField()

    def get_teachers(self,obj):
        teachers_obj = TeacherSerializer(obj.teachers,many=True)
        return teachers_obj.data

    def get_scholarship(self,obj):
        scholarship_obj = obj.scholarship_set.all().values('time_percent','value')
        return scholarship_obj

    def get_model_name(self,obj):
        modelname = obj.course_set.all().values('name')
        return modelname