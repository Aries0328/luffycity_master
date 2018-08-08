from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ViewSetMixin
from api.models import Course
from api.utils.response import BaseResponse

shoppingcar = []

class ShoppingView(ViewSetMixin,APIView):
    def create(self,request,*args,**kwargs):
        res = BaseResponse()
        course_id = request.data.get('courseId')
        valid_period = request.data.get('valid_period_day')

        course_obj = Course.objects.get(id = course_id)
        valid_period_list = course_obj.price_policy.all().values('valid_period','price')
        for i in valid_period_list:
            if int(valid_period) == i['valid_period']:
                user = {'userid':1,'course':{'course_id':course_obj.id,'course_name':course_obj.name,'price':i['price'],'price_list':list(valid_period_list)}}
                shoppingcar.append(user)
                res.data = '数据获取成功'
                break
        else:
            res.code = 500
            res.error = '数据不存在'
        print(shoppingcar)
        return Response(res.dict)

    def update(self,request,*args,**kwargs):
        '''
        验证:获取的新数据,旧数据都要存在于数据库


        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        res = BaseResponse()
        course_id = request.data.get('courseId')
        valid_period_new = request.data.get('valid_period_day_new')
        valid_period_old = request.data.get('valid_period_day_old')


    def destroy(self,request,*args,**kwargs):
        '''
        只要id
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        pass