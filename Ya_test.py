import unittest
from YaDisk import YandexDisk

ya = YandexDisk(token='')

class YaDiskTests(unittest.TestCase):

    def test_creat_folders_code201(self):
        self.assertEqual(ya.creat_folders('test', 'Photos'), f'Creating folder "Photos":201')
    def test_creat_folders_code409(self):
        self.assertEqual(ya.creat_folders('test', 'Photos'), f'Folder "Photos" already exist:409')
    def test_creat_folders_code404(self):
        self.assertEqual(ya.creat_folders('', 'Photo'), f'Error:404')

if __name__ == '__main__':
    unittest.main()