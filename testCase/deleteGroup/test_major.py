import time
import unittest
from copy import deepcopy
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead

@class_case_log
class DeleteGroup(unittest.TestCase):
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

    def testCase01_major(self):
        """新增分组主流程"""
        step('请求新增分组')
        path = '/v3/notesvr/set/notegroup'
        group_id = str(int(time.time() * 1000)) + '_groupId'
        self.data['groupId'] = group_id
        self.data=deepcopy(self.data)
        res = post(url=self.host + path, data=self.data, sid=self.sid1, userid=self.userid1)

        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'updateTime': int
        }
        OutPutCheck().output_check(expect=expect, actual=res.json())
        step('请求获取分组信息接口，校验数据源的正确性')

