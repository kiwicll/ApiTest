import requests
from common.logsMethod import info, error


def get(url, sid, headers=None):
    if headers is None:
        headers = {
            'Cookie': f'wps_sid={sid}'
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    try:
        res = requests.get(url=url, headers=headers, timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return "requests timeout!"
    info(f'【requests】code:{res.status_code}')
    info(f'【requests】body:{res.text}')
    return res


def post(url, data, sid, userid, headers=None):
    if headers is None:
        headers = {
            'Cookie': f'wps_sid={sid}',
            'X-user-key': f'{userid}'
        }
    info(f'【requests】url:{url}')
    info(f'【requests】headers:{headers}')
    info(f'【requests】body:{data}')
    try:
        res = requests.post(url=url, headers=headers, json=data, timeout=30)
    except TimeoutError:
        error('requests timeout!')
        return "requests timeout!"
    info(f'【requests】code:{res.status_code}')
    info(f'【requests】body:{res.text}')
    return res
