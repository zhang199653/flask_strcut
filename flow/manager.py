# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 14:25
# @Author  : Zcs
# @File    : manager.py
from flask import Blueprint
from flask_restful import Api
from flow.view.urls import urls

"""
生成蓝图对象，并生成api
蓝图会记录添加的所有函数，当以后注册蓝图时，这些函数会被注册到应用
"""

BG_MANAGER = Blueprint("flow", __name__)  # 生成一个蓝图对象
api = Api(BG_MANAGER)  # 为蓝图对象生成api，restful_api可以为flask对象和蓝图对象生成api

#  加载该模块所有的api
for cls_path, url_path in urls:
    cls_name = cls_path.split('.')[1]  # 类名

    #  由于在外层的bg_manager要加载该py文件，所以module_path要使用绝对路径
    module_path = 'flow.view.%s' % cls_path.split('.')[0]  # 得到模块路径
    module = __import__(module_path, fromlist=True)  # 导入api_cls.py
    cls = getattr(module, cls_name)
    api.add_resource(cls, url_path, endpoint=url_path)
