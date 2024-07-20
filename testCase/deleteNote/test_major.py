import time
import unittest
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead
from business.dataCreate import CreatNote


@class_case_log
class DeleteNote(unittest.TestCase):
    # 定义实例方法名称，相当于用例名称
    envConfig = YamlRead().env_config()
    dataConfig = YamlRead().data_config()['deleteNote']
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']
    deleteNoteUrl = host + path




    # def setUp(self):
    #     step('清空用户分组数据')
    #     DataClear().group_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """新增便签主体主流程"""
        step('构建便签数据')

        note=CreatNote().create_note(user_id=self.userid1, sid=self.sid1, num=1)
        print(note)
        noteId = note[0]['noteId']

        step('请求删除便签主体')
        body = {
            'noteId':noteId
        }
        # 将生成的noteId赋值给body字典中的'noteId'键
        res = post(url=self.deleteNoteUrl, data=body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())
