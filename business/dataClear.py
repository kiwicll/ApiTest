import requests


class DataClear:
    def group_clear(self, sid, user_id):
        url = 'http://note-api.wps.cn/v3/notesvr/get/notegroup'
        header = {
            'Cookie': f'wps_sid={sid}',
            'X-user-key':f'{user_id}'
        }
        data = {'excludeInvalid': True}
        get_res = requests.post(url, headers=header, json=data)
        print(get_res.json())
        print(len(get_res.json()['noteGroups']))
        # 获取返回中的分组信息，提取groupid
        for group in get_res.json()['noteGroups']:
            group_id = group['groupId']

            # 调取删除接口，删除该用户全部的有效分组
            del_url = 'https://note-api.wps.cn/notesvr/delete/notegroup'
            data = {'groupId': group_id}
            del_res = requests.post(url=del_url, headers=header, json=data)
            #print(del_res.status_code)
            if del_res.status_code != 200:
                return False

        # 再次获取分组信息，确认删除
        get_res = requests.post(url, headers=header, json=data)
        print("Groups after deletion:", get_res.json())
        print("Group count after deletion:", len(get_res.json()['noteGroups']))

        return len(get_res.json()['noteGroups']) == 0


if __name__ == '__main__':
    ress = DataClear().group_clear('V02SvflNl5fzuIX6IfG-UybIXNzzIJU00af1be53001a32de1c', '439541276')
    print("All groups deleted:", ress)
    #待补充包含便签内容的数据删除
