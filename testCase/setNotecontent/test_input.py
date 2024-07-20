import time
import unittest
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import post
from business.dataClear import DataClear
from common.yamlRead import YamlRead
from common.AES_CBC import EncryptDate


@class_case_log
class SetNoteContentInput(unittest.TestCase):
    # 从配置文件读取环境和数据配置
    envConfig = YamlRead().env_config()
    # 主体环境数据
    dataConfig = YamlRead().data_config()['createNote']
    path = dataConfig['path']

    # 内容环境数据
    dataConfig2 = YamlRead().data_config()['createNoteContent']
    path2 = dataConfig2['path']

    # 初始化所需的参数
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    setNoteUrl = host + path
    setNoteContentUrl = host + path2

    # 准备请求体数据
    Note_body = {
        'noteId': str(int(time.time() * 1000)) + '_noteId',
        'star': 0,
        'remindType': 0,
        'groupId': '001'
    }
    content_body = {
        'noteId': f'{Note_body['noteId']}',
        'title': "title_test",
        'summary': "summary_test",
        'body': 'body_test',
        'localContentVersion': 1,
        'BodyType': 0
    }

    # 读取加密配置
    epConfig = YamlRead().encryption_config()['encryption']
    key = epConfig['key']
    iv = epConfig['iv']


    # def setUp(self):
    #     step('清空用户分组数据')
    #     DataClear().group_clear(sid=self.sid1, user_id=self.userid1)


    def testCase01_remove_key(self):
        """新增便签主体主流程,移除必填项noteId"""
        step('请求新增便签内容')
        try:
            # 移除 noteId 字段
            self.content_body.pop('noteId')

            # 加密请求体中的字段
            step("入参加密")
            self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])


            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase02_empty_key(self):
        """新增便签主题主流程,必填项noteId为空"""
        step('请求新增便签内容')

        try:
            # 移必填项noteId为空
            self.content_body['noteId'] = ''

            # 加密请求体中的字段
            step("入参加密")
            self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])


            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase03_None_key(self):
        """新增便签主题主流程,必填项noteId为None"""
        step('请求新增便签内容')

        try:
            # 移必填项noteId为空
            self.content_body['noteId'] = None

            # 加密请求体中的字段
            step("入参加密")
            self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])

            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")
    def testCase04_remove_key(self):
        """新增便签主题主流程,移除必填项body"""
        step('请求新增便签主体')
        res = post(url=self.setNoteUrl, data=self.Note_body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'infoVersion': int,
            'infoUpdateTime': int
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())

        step('请求新增便签内容')
        try:

            # 加密请求体中的字段
            step("入参加密")
            self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])

            # 移除 noteId 字段
            self.content_body.pop('body')

            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')

        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase05_empty_key(self):
        """新增便签主题主流程,必填项body为空"""
        step('请求新增便签主体')
        res = post(url=self.setNoteUrl, data=self.Note_body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'infoVersion': int,
            'infoUpdateTime': int
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())

        step('请求新增便签内容')
        try:
            # 移必填项body为空
            self.content_body['body'] = ''

            # 加密请求体中的字段
            step("入参加密")
            self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])

            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase06_None_key(self):
        """新增便签主题主流程,必填项body为None"""
        step('请求新增便签主体')
        res = post(url=self.setNoteUrl, data=self.Note_body, sid=self.sid1, userid=self.userid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'infoVersion': int,
            'infoUpdateTime': int
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())
        step('请求新增便签内容')

        try:
            # 移必填项body为空
            self.content_body['body'] = None

            # 加密请求体中的字段
            step("入参加密")
            #self.content_body['body'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['body'])
            self.content_body['title'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['title'])
            self.content_body['summary'] = EncryptDate(self.key, self.iv).encrypt(self.content_body['summary'])

            # 发送POST请求
            res = post(url=self.setNoteContentUrl, data=self.content_body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")