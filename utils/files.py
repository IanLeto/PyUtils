# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 2:23 下午
# @Author  : Ian Leto
# @File    : files.py
# 干啥的    :
import json, os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def conv_jsonfile(path: str) -> dict:
    with open(path) as json_file:
        return json.load(json_file)
