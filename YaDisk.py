import requests

class YandexDisk:

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def creat_folders(self, disk_file_path, folder_name):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": '/' + disk_file_path + '/' + folder_name}
        response = requests.put(files_url, headers=headers, params=params)
        print(response)
        if response.status_code == 201:
            return f'Creating folder "{folder_name}":' + str(response.status_code)
        elif response.status_code == 409:
            return f'Folder "{folder_name}" already exist:' + str(response.status_code)
        else:
            return 'Error:' + str(response.status_code)

# TOKEN = ''
#
# if __name__ == '__main__':
#     ya = YandexDisk(token=TOKEN)
#     print(ya.creat_folders('', 'P3'))
