import unittest
import os
from BeautifulReport import BeautifulReport


DIR = os.path.dirname(os.path.abspath(__file__))
#Online 线上环境，Offline测试环境
ENVIRON='Offline'


if __name__ == '__main__':
    #定义执行的优先级
    run_pattern = 'all'

    if run_pattern == 'all':
        pattern = 'test_*.py'

    elif run_pattern == 'smoking':
        pattern = 'test_major*.py'
    else:
        run_pattern = run_pattern + '.py'

    suite = unittest.TestLoader().discover('./testCase', pattern='test*.py')

    # runner = unittest.TextTestRunner()
    # runner.run(suite)

    result = BeautifulReport(suite)
    result.report(filename="report.html", description='测试报告', report_dir='./')
