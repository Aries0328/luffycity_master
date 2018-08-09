from django.conf.urls import url
from api.views import course
# from api.views import auth
from api.views import shoppingcart


urlpatterns = [
    url(r"courses/", course.CoursesView.as_view()),
    url(r"all_degreecourse_teacher/", course.AllDcourseTeacher.as_view()),
    url(r"all_degreecourse_scholarship/", course.AllDegreecourseScholarship.as_view()),
    url(r"all_course/", course.AllCourse.as_view()),
    url(r"degreecourse_modulename/(?P<pk>\d+)/", course.DegreecourseModule.as_view()),
    url(r"course_detail/(?P<pk>\d+)/", course.CourseDetail.as_view()),
    url(r"course_qa/(?P<pk>\d+)/", course.CourseQuestion.as_view()),
    url(r"course_outline/(?P<pk>\d+)/", course.CourseOutline.as_view()),
    url(r"course_chapter/(?P<pk>\d+)/", course.CourseChapter.as_view()),
    url(r"shopcart/$",shoppingcart.ShoppingCarView.as_view({"post": "create", "get": "list", "delete": "destroy", "put": "update"})),
]