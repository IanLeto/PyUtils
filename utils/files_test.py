# -*- coding: utf-8 -*-
# @Time    : 2022/1/11 2:26 下午
# @Author  : Ian Leto
# @File    : files_test.py
# 干啥的    :
import unittest
from . import files


class Files(unittest.TestCase):
    def test_load_json(self):
        self.assertEqual('v', files.conv_jsonfile(files.ROOT_PATH + '/data.json')['key'])


if __name__ == '__main__':
    unittest.main()
