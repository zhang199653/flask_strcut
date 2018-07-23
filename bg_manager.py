# -*- coding: utf-8 -*-
# @Time    : 2018/7/23 16:59
# @Author  : Zcs
# @File    : bg_manager.py

from blue_print.blue_urls import blue_list
from flask import Flask

"""
管理所有蓝图
"""

app = Flask(__name__)
app.debug = True


def main():
    for module_path, blue in blue_list:
        module = __import__(module_path, fromlist=True)
        blue_obj = getattr(module, blue)  # 各个APP中的蓝图对象
        app.register_blueprint(blue_obj)  # 注册蓝图
        app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
