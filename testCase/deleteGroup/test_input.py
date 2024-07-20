import time
import unittest
from copy import deepcopy
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead

@class_case_log
class DeleteGroupInput(unittest.TestCase):
    # 定义实例方法名称，相当于用例名称
    userid1 = '439541276'
    sid1 = 'V02SvflNl5fzuIX6IfG-UybIXNzzIJU00af1be53001a32de1c'
    host = 'http://note-api.wps.cn'
    data = {
        'groupId': 'group_id',
        'groupName': 'NAME0601',
        'order': 0
    }
    def setUp(self):
        step('清空用户分组数据')
        DataClear().group_clear(self.sid1,self.userid1)

    def testCase01_remove_input(self):
        """新增分组主流程,必填项缺失"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        #深拷贝过后来删除必填项
        self.data=deepcopy(self.data)
        self.data.pop('groupId')

        res = post(url=self.host + path, data=self.data, sid=self.sid1, userid=self.userid1)

        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'updateTime': int
        }
        OutPutCheck().output_check(expect=expect, actual=res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase02_empty_input(self):
        """新增分组主流程,必填项为空"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        #深拷贝过后来删除必填项
        self.data=deepcopy(self.data)
        self.data['groupId']=''

        res = post(url=self.host + path, data=self.data, sid=self.sid1, userid=self.userid1)

        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'updateTime': int
        }
        OutPutCheck().output_check(expect=expect, actual=res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

    def testCase03_None_input(self):
        """新增分组主流程,必填项None"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        #深拷贝过后来删除必填项
        self.data=deepcopy(self.data)
        self.data['groupId']=None

        res = post(url=self.host + path, data=self.data, sid=self.sid1, userid=self.userid1)

        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'updateTime': int
        }
        OutPutCheck().output_check(expect=expect, actual=res.json())
        step('请求获取分组信息接口，校验数据源的正确性')