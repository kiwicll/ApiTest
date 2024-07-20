import time
import unittest

from common.logsMethod import step, class_case_log
from business.apiRe import post
from common.yamlRead import YamlRead


@class_case_log
class GetNoteBodyInput(unittest.TestCase):
    # 从配置文件读取环境和数据配置
    envConfig = YamlRead().env_config()
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']


    # 获取便签内容
    dataConfig = YamlRead().data_config()['getNoteBody']
    path = dataConfig['path']
    mustKeys2 = dataConfig['mustKeys']

    getNoteBodyUrl = host + path

    def testCase01_remove_input(self):
        # 获取便签内容
        """获取便签内容,必填项缺失"""
        step('请求获取便签内容')
        body = {'noteIds': 'noteId'}
        #移除noteIds
        body.pop('noteIds')
        try:
            # 发送POST请求
            res = post(url=self.getNoteBodyUrl, data=body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase02_empty_input(self):
        """获取便签内容,必填项empty"""
        # 获取便签内容
        step('请求获取便签内容')
        body = {'noteIds': ''}
        try:
            # 发送POST请求
            res = post(url=self.getNoteBodyUrl, data=body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")

    def testCase03_None_input(self):
        """获取便签内容,必填项empty"""
        step('请求获取便签内容')
        body = {'noteIds': None}
        # noteIds为空
        try:
            # 发送POST请求
            res = post(url=self.getNoteBodyUrl, data=body, sid=self.sid1, userid=self.userid1)
            self.assertEqual(500, res.status_code, msg=f'code:{res.status_code}状态码异常')
        except Exception as e:
            self.fail(f"测试用例执行失败: {str(e)}")