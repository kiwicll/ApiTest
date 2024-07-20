import unittest

class OutPutCheck(unittest.TestCase):

    def output_check(self, expect, actual):
        """
        通用断言方法
        :param expect: 期望值，一object结构描述出期望值，支持动态值的校验和精准值的校验
        :param actual: 实际值 字典结构的json字符串 一般来说指的是response.json()
        :return:
        """
        # 判断返回值的字段长度
        self.assertEqual(len(expect.keys()), len(actual.keys()), msg='Key length mismatch')

        # 遍历期望值中的字典结构
        for k, v in expect.items():
            # 判断返回值是否存在
            self.assertIn(k, actual.keys(), msg=f'Expected key: 【{k}】 not in response')
            if isinstance(v, type):
                # 判断期待值与实际值类型是否一致
                self.assertEqual(v, type(actual[k]), msg=f'Key: 【{k}】 type mismatch')
            elif isinstance(v, dict):
                # 如果返回值类型是字典类型，则通过递归再次校验
                self.output_check(v, actual[k])
            elif isinstance(v, list):
                # 如果返回值类型是列表类型
                # 判断列表长度
                if len(v) == 1 and isinstance(v[0], dict):
                    # 处理查询接口返回的多个字典的情况
                    for actual_item in actual[k]:
                        self.output_check(v[0], actual_item)
                else:
                    self.assertEqual(len(v), len(actual[k]), msg=f'Key: 【{k}】 list length mismatch')
                    # 遍历列表中的每个元素
                    for i in range(len(v)):
                        # 判断列表中元素的类型
                        if isinstance(v[i], type):
                            self.assertEqual(v[i], type(actual[k][i]), msg=f'List item index {i}: type mismatch')
                        elif isinstance(v[i], dict):
                            self.output_check(v[i], actual[k][i])
                        else:
                            self.assertEqual(v[i], actual[k][i], msg=f'List item index {i}: value mismatch')
            else:
                # 判断其他类型的值
                self.assertEqual(v, actual[k], msg=f'Key: 【{k}】 value mismatch')
