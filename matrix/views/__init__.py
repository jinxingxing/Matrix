# coding:utf8
# 尝试实现 views 自动加载
# 运行正常但，无法正常访问，访问任何地址都是一直 loading，可能是循环引用的问题？？
# import os
# import importlib
#
# cwd = os.getcwd()
# for filename in filter(lambda s: s.endswith(".py") and not s.startswith("_"), os.listdir(cwd)):
#     modname = os.path.splitext(filename)[0]
#     importlib.import_module(modname)

import area
import hello
import index
import user