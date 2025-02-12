import functools
import inspect
import os
from datetime import datetime
from colorama import Fore
from main import DIR


def info(text):
    stack = inspect.stack()
    # 定义当前输出时间
    formatter_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    # 当前执行文件的绝对路径和执行代码行号
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"
    content = f"[INFO]{formatter_time}-{code_path}>>{text}"
    print(Fore.LIGHTGREEN_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')

def error(text):
    stack = inspect.stack()
    # 定义当前输出时间
    formatter_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    # 当前执行文件的绝对路径和执行代码行号
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"
    content = f"[ERROR]{formatter_time}-{code_path}>>{text}"
    print(Fore.LIGHTGREEN_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')
    with open(file=DIR + '\\logs\\' + f'{str_time}_error.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')

def step(text):
    stack = inspect.stack()
    # 定义当前输出时间
    formatter_time = datetime.now().strftime('%H:%M:%S:%f')[:-3]
    # 当前执行文件的绝对路径和执行代码行号
    code_path = f"{os.path.basename(stack[1].filename)}:{stack[1].lineno}"
    content = f"[STEP]{formatter_time}-{code_path}>>{text}"
    print(Fore.LIGHTGREEN_EX + content)
    str_time = datetime.now().strftime("%Y%m%d")
    with open(file=DIR + '\\logs\\' + f'{str_time}_info.log', mode='a', encoding='utf-8') as f:
        f.write(content + '\n')

def case_log_init(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        #获取类名
        class_name=args[0].__class__.__name__
        #获取方法名
        method_name=func.__name__
        #获取方法注释
        docstring=inspect.getdoc(func)
        print(Fore.LIGHTRED_EX+'-------------------------------------------------------------------------')
        info(f"Class Name:{class_name}")
        info(f"Method Name:{method_name}")
        info(f"Test Description:{docstring}")
        func(*args,**kwargs)
    return inner

def class_case_log(cls):
    """用例的日志装饰器级别 """
    for name,method in inspect.getmembers(cls,inspect.isfunction):
        if name.startswith('testCase'):
            setattr(cls,name,case_log_init(method))
    return cls