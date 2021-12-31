# -*- coding: utf-8 -*-
# @Time    : 2021/12/30 4:20 下午
# @Author  : Ian Leto
# @File    : reg.py
# 干啥的    : 正则

import re

labels = [
    'x.json', 'region_111', 'x.json2', 'project_id_template.json'
]


# 前缀
def prefix_re():
    print([i for i in labels if re.search(r"\.*.json", i)])


# 截取前缀
def split_prefix(value: str, word: str) -> str:
    ephemeral = value.split(word)
    if len(ephemeral) > 0:
        return ephemeral[0]
    return ""


if __name__ == '__main__':
    print(split_prefix('project_id_template.json', '_template'))
