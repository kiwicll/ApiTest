import requests
import time


class CreatNote:
    host = 'http://note-api.wps.cn'

    def create_note(self, user_id, sid, num):
        # 定义空便签列表，可将新建后的便签存放至此，以便其他接口调用
        notes_list = []
        # 新建便签主体
        # num-1新建的便签主题数
        for i in range(num):
            headers = {
                'Content-Type': 'application/json',
                'Cookie': f'wps_sid={sid}',
                'X-user-key': str(user_id)
            }
            # 添加时间戳，生成唯一的note_id
            note_id = str(int(time.time() * 1000)) + '_noteId'

            body = {
                'noteId': note_id
            }
            res = requests.post(url=self.host + '/v3/notesvr/set/noteinfo', headers=headers, json=body)

            # 在新建的便签主题里新建便签内容，
            infoVersion = res.json()['infoVersion']
            body = {
                'noteId': note_id,
                'title': 'test_title',
                'summary': 'test_summary',
                'body': 'test_body',
                'localContentVersion': infoVersion,
                'BodyType': 0
            }
            notes_list.append(body)
            requests.post(url=self.host + '/v3/notesvr/set/notecontent', headers=headers, json=body)
        return notes_list
