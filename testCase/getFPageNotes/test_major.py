import time
import unittest
from common.logsMethod import step, class_case_log
from common.checkoutput import OutPutCheck
from business.apiRe import get
from business.dataClear import DataClear
from common.yamlRead import YamlRead
from common.AES_CBC import EncryptDate


@class_case_log
class GetPageNote(unittest.TestCase):

    # 从配置文件读取环境和数据配置
    envConfig = YamlRead().env_config()

    # 初始化所需的参数
    userid1 = envConfig['userid1']
    sid1 = envConfig['sid1']
    host = envConfig['host']

    def testCase01_major(self):
        """获取首页便签主流程"""

        startindex=0
        rows=10
        getPageNoteUrl = self.host + f'/v3/notesvr/user/{self.userid1}/home/startindex/{startindex}/rows/{rows}/notes'
        step('请求新增便签主体')

        # 将生成的noteId赋值给body字典中的'noteId'键
        res = get(url=getPageNoteUrl, sid=self.sid1)
        self.assertEqual(200, res.status_code, msg=f'code:{res.status_code}状态码异常')
        expect = {
            'responseTime': int,
            'webNotes': [{
                'noteId':str,
                'createTime': int,
                'star':int,
                'remindTime':int,
                'remindType':int,
                'infoVersion':int,
                'infoUpdateTime':int,
                'groupId':str,
                'title':str,
                'summary':str,
                'thumbnail':str,
                'contentVersion':int,
                'contentUpdateTime':int,
            }]
        }
        step('请求获取分组信息接口，校验数据源的正确性')
        OutPutCheck().output_check(expect=expect, actual=res.json())