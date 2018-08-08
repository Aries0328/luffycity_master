from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from api.views import course,shoppingcart

#
#
# urlpatterns = [
#     # url(r'degreecourses/',views.Courses.as_view())
# ]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls


urlpatterns = [
    url(r'courselist/$',course.CourseView.as_view({'get':'create'})),
    url(r'courselist/(?P<pk>\d+)/$',course.CourseView.as_view({'get':'retrieve'})),

    url(r'degreecourse/$',course.DegreeCourseView.as_view({'get':'create'})),
    url(r'degreecourse/(?P<pk>\d+)/$',course.DegreeCourseView.as_view({'get':'retrieve'})),

    url(r'coursemodel/$',course.CourseModelView.as_view({'get':'create'})),
    url(r'coursemodel/(?P<pk>\d+)/$',course.CourseModelView.as_view({'get':'retrieve'})),

    url(r'shoppingcar/$',shoppingcart.ShoppingView.as_view({'post':'create','put':'update','delete':'destroy'}))
]