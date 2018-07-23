# -*- coding: utf-8 -*-
# @Time    : 2018/7/17 18:00
# @Author  : Zcs
# @File    : api_cls.py.py

"""
存放flask restful_api 类
"""
from flask_restful import Resource


class FlowOne(Resource):
    def get(self):
        return 'FlowOneGet'

    def post(self):
        return 'FlowOnePost'

    def put(self):
        return 'FlowOnePut'

    def delete(self):
        return 'FlowOneDel'


class FlowTwo(Resource):
    def get(self):
        return 'FlowTwoGet'

    def post(self):
        return 'FlowTwoPost'

    def put(self):
        return 'FlowTwoPut'

    def delete(self):
        return 'FlowTwoDel'
