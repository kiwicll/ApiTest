import time
import unittest

from common.AES_CBC import EncryptDate
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead


@class_case_log
class GetNoteBody(unittest.TestCase):
    # # 从配置文件读取环境和数据配置
    envConfig = YamlRead().env_config()
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    #新增便签内容数据配置
    dataConfig = YamlRead().data_config()['createNoteContent']
    path = dataConfig['path']
    mustKeys = dataConfig['mustKeys']

   #获取便签内容数据配置
    dataConfig2 = YamlRead().data_config()['getNoteBody']
    path2 = dataConfig2['path']
    mustKeys2 = dataConfig2['mustKeys']

    setNoteContentUrl = host + path
    getNoteBodyUrl = host + path2


    # 读取加密配置
    epConfig = YamlRead().encryption_config()['encryption']
    key = epConfig['key']
    iv = epConfig['iv']

    # def setUp(self):
    #     step('清空用户分组数据')
    #     DataClear().group_clear(sid=self.sid1, user_id=self.userid1)

    def testCase01_major(self):
        """获取便签内容主流程"""
        step('请求获取便签内容')
        # 准备请求体数据
        body = {
            'noteId': str(int(time.time() * 1000)) + '_noteId',
            'title': "title_test",
            'summary': "summary_test",
            'body': 'body_test',
            'localContentVersion': 1,
            'BodyType': 0
        }

        try:
            # 加密请求体中的字段
            step("入参加密")
            body['body'] = EncryptDate(self.key, self.iv).encrypt(body['body'])
            body['title'] = EncryptDate(self.key, self.iv).encrypt(body['title'])
            body['summary'] = EncryptDate(self.key, self.iv).encrypt(body['summary'])

            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')

            # 预期响应字段
            expect = {
                'responseTime': int,
                'contentVersion': int,
                'contentUpdateTime': int
            }

            # 校验响应数据
            step('请求获取分组信息接口，校验数据源的正确性')
            OutPutCheck().output_check(expect=expect, actual=res.json())
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

        """获取便签内容主流程"""
        #获取便签内容
        step('请求获取便签内容')
        body2 = {'noteIds': [body['noteId']]}
        try:
            # 发送POST请求
            res = post(url=self.getNoteBodyUrl, data=body2, sid=self.sid1, userid=self.userid1)
            self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')

            # 解密请求体中的字段
            step("返回体解密")
            note_body = res.json()['noteBodies'][0]
            note_body['body'] = EncryptDate(self.key, self.iv).decrypt(note_body['body'])
            note_body['title'] = EncryptDate(self.key, self.iv).decrypt(note_body['title'])
            note_body['summary'] = EncryptDate(self.key, self.iv).decrypt(note_body['summary'])

            print(note_body['body'])
            print(note_body['title'])
            print(note_body['summary'])

            # 预期响应字段
            expect = {
                'responseTime': int,
                'noteBodies': [{
                    'summary': "summary_test",
                    'noteId': body['noteId'],
                    'bodyType': int,
                    'body': 'body_test',
                    'contentVersion': 1,
                    'contentUpdateTime': int,
                    'title': "title_test",
                    'valid': 1

                }]
            }
            # 校验响应数据
            step('请求获取分组信息接口，校验数据源的正确性')
            OutPutCheck().output_check(expect=expect, actual=res.json())
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

