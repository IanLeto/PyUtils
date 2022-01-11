# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 2:13 下午
# @Author  : Ian Leto
# @File    : exec.py
# 干啥的    : python 执行git
import subprocess


def demo(content: str):
    try:
        s = subprocess.run(content, shell=True, timeout=10, stdout=open('stdout.txt', 'w'),
                           stderr=open('stderr.txt', 'w'))
    except Exception as e:
        print(e)
    return s.returncode


if __name__ == '__main__':
    demo('ls')
