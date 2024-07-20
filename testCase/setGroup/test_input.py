import time
import unittest
from copy import deepcopy
from common.logsMethod import step, class_case_log
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead
from parameterized import parameterized


@class_case_log
class SetGroupInput(unittest.TestCase):
    # 定义实例方法名称，相当于用例名称
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['createGroup']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']
    setGroupUrl = host + path
    data = {
        'groupId': 'group_id',
        'groupName': 'NAME0601',
        'order': 0
    }

    def setUp(self):
        step('清空用户分组数据')
        DataClear().group_clear(sid=self.sid1, user_id=self.userid1)

    @parameterized.expand(mustKeys)
    def testCase01_remove_key(self, key):
        """新增分组主流程,groupId&groupName必填项缺失"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        # 深拷贝过后来删除必填项
        body = deepcopy(self.data)
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # 将生成的groupId赋值给body字典中的'groupId'键
        body['groupId'] = group_id
        body.pop(key)
        res = post(url=self.host + path, data=body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

    @parameterized.expand(mustKeys)
    def testCase02_empty_key(self, key):
        """新增分组主流程,groupId&groupName必填项为空"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        # 深拷贝过后来删除必填项
        body = deepcopy(self.data)
        group_id = str(int(time.time() * 1000)) + '_groupId'
        # 将生成的groupId赋值给body字典中的'groupId'键
        body['groupId'] = group_id
        body['key'] = ''
        res = post(url=self.host + path, data=body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

    @parameterized.expand(mustKeys)
    def testCase03_key_None(self, key):
        """新增分组主流程,groupId&groupName必填项为None"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'

        # 深拷贝过后来删除必填项
        body = deepcopy(self.data)
        group_id = str(int(time.time() * 1000)) + '_groupId'

        # 将生成的groupId赋值给body字典中的'groupId'键
        body['groupId'] = group_id
        body['key'] = None

        res = post(url=self.host + path, data=body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
