import time
import unittest
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead


@class_case_log
class SetNote(unittest.TestCase):
    # 定义实例方法名称，相当于用例名称
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['createNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']
    setNoteUrl = host + path


    # def setUp(self):
    #     step('清空用户分组数据')
    #     DataClear().group_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """新增便签主体主流程"""
        step('请求新增便签主体')
        body = {
            'noteId':'_noteId',
            'star':0,
            'remindType':0,
            'groupId':'001'
        }
        # 将生成的noteId赋值给body字典中的'noteId'键
        noteId = str(int(time.time() * 1000)) + '_noteId'
        body['noteId'] = noteId
        res = post(url=self.setNoteUrl, data=body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'infoVersion':int,
            'infoUpdateTime': int
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())
