import unittest
from YaDisk import YandexDisk

ya = YandexDisk(token='')

class YaDiskTests(unittest.TestCase):

    def test_creat_folders_code201(self):
        self.assertEqual(ya.creat_folders('Photos'), f'Creating folder "Photos":201')
    def test_creat_folders_code409(self):
        self.assertEqual(ya.creat_folders('Photos'), f'Folder "Photos" already exist:409')

if __name__ == '__main__':
    unittest.main()