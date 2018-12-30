from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serialize.modelserialize import *

# Create your views here.
# class CourseView(APIView):
#     def get(self, request, *args, **kwargs):
#         # print(request.version)
#         ret = {'code': 1000, 'data': None}
#         try:
#             course_obj = Course.objects.all()
#             ser = CourseModelSerialize(course_obj, many=True)
#             ret['data'] = ser.data
#         except Exception as e:
#             ret['code'] = 1001
#             ret['error'] = '获取失败'
#
#         return Response(ret)
from rest_framework.viewsets import GenericViewSet, ViewSetMixin  # 但凡是继承了ViewSetMixin就可以使用新的as_view，可以路由中可以传入字典


class CourseView(ViewSetMixin, APIView):
    authentication_classes = []

    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            course_obj = Course.objects.all()
            ser = CourseModelSerialize(course_obj, many=True)
            ret['data'] = ser.data
        except Exception as e:
            print('课程获取失败')
            ret['code'] = 1001
            ret['error'] = '获取失败'
        return Response(ret)


class CourseDetailView(ViewSetMixin, APIView):
    authentication_classes = []

    def retreive(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        try:
            pk = kwargs.get('pk')
            # print(pk)
            course_obj = CourseDetail.objects.filter(course_id=pk).first()
            print(course_obj)
            ser = CourseDetailModelSerialize(course_obj, many=False)
            print(ser.data)
            ret['data'] = ser.data
        except Exception as e:
            print('课程详细获取失败')
            ret['code'] = 1001
            ret['error'] = '获取失败'
        return Response(ret)


class AuthView(APIView):
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        res = {"code": 1000, "msg": None}
        try:
            print(request.data)
            # user = request._request.POST.get("user")
            # pwd = request._request.POST.get("password")
            user = request.data.get('username')
            pwd = request.data.get('password')
            user_obj = UserInfo.objects.filter(username=user, password=pwd).first()
            print(user, pwd, user_obj)
            if not user_obj:
                res["code"] = 1001
                res["msg"] = "用户名或者密码错误"
            else:
                # token = get_random_str(user)
                import uuid
                token = str(uuid.uuid4())
                Token.objects.update_or_create(username=user_obj,
                                               defaults={"token": token})  # 有这个user就更新token，没有就创建user
                res["token"] = token

        except Exception as e:
            res["code"] = 1002
            res["msg"] = e
        return Response(res)
        # return JsonResponse(res, json_dumps_params={"ensure_ascii": False})


class MicroView(ViewSetMixin, APIView):
    def list(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': '很好'}
        # try:
        #     course_obj = Course.objects.all()
        #     ser = CourseModelSerialize(course_obj, many=True)
        #     ret['data'] = ser.data
        # except Exception as e:
        #     ret['code'] = 1001
        #     ret['error'] = '获取失败'
        return Response(ret)
