from main import DIR,ENVIRON
import yaml

class YamlRead:
    @staticmethod
    def env_config():
        with open(file=f'{DIR}/config/env/{ENVIRON}/config.yml',mode='r',encoding='utf-8') as f:
           return  yaml.load(f,Loader=yaml.FullLoader)

    @staticmethod
    def data_config():
        with open(file=f'{DIR}/config/data/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)

    @staticmethod
    def encryption_config():
        with open(file=f'{DIR}/config/encryption/config.yml', mode='r', encoding='utf-8') as f:
            return yaml.load(f, Loader=yaml.FullLoader)
        # # 从YAML文件中读取配置
        # with open('config.yaml', 'r') as file:
        #     config = yaml.safe_load(file)
        #     key = config['encryption']['key']
        #     iv = config['encryption']['iv']