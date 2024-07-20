import time
import unittest
from parameterized import parameterized
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead


@class_case_log
class SetNoteInput(unittest.TestCase):
    # 从配置文件读取环境和数据配置
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['createNote']

    # 初始化所需的参数
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']
    setNoteUrl = host + path
    body = {
        'noteId': '_noteId',
        'star': 0,
        'remindType': 0,
        'groupId': '001'
    }

    @parameterized.expand(mustKeys)
    def testCase01_remove_key(self,key):
        """新增便签主体,必填项缺失"""
        step('请求新增便签主体')
        self.body.pop(key)
        res = post(url=self.setNoteUrl, data=self.body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

    @parameterized.expand(mustKeys)
    def testCase02_empty_key(self, key):
        """新新增便签主体,必填项值为空"""
        step('请求新增便签主体')
        self.body['key'] = ''
        res = post(url=self.setNoteUrl, data=self.body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

    @parameterized.expand(mustKeys)
    def testCase03_None_key(self, key):
        """新增便签主体,必填项为None"""
        step('请求新增便签主体')
        self.body['key'] = None
        res = post(url=self.setNoteUrl, data=self.body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

