import unittest
from app import get_name_by_document_number, get_shelf_by_document_number
from app import add_document_and_put_on_shelf, delete_document_and_put_off_shelf, add_shelf

class TestSomething(unittest.TestCase):

    #get_name_by_document_number
    def test_get_name_Equal(self):
        self.assertEqual(get_name_by_document_number('10006'), 'Аристарх Павлов')
    def test_get_name_NotEqual_T1(self):
        self.assertNotEqual(get_name_by_document_number('10006'), 'Геннадий Покемонов')
    def test_get_name_NotEqual_T2(self):
        self.assertNotEqual(get_name_by_document_number(' '), 'Геннадий Покемонов')
    def test_get_name_NotEqual_T3(self):
        self.assertNotEqual(get_name_by_document_number('11-2'), 'Аристарх Павлов')

    #get_shelf_by_document_number
    def test_get_shelf_Equal(self):
        self.assertEqual(get_shelf_by_document_number('10006'), '2')
    def test_get_shelf_NotEqual_T1(self):
        self.assertNotEqual(get_shelf_by_document_number('10006'), '1')
    def test_get_shelf_NotEqual_T2(self):
        self.assertNotEqual(get_shelf_by_document_number('11-2'), '2')
    def test_get_shelf_NotEqual_T3(self):
        self.assertNotEqual(get_shelf_by_document_number(' '), '1')

    #add_document_and_put_on_shelf
    def test_add_document_Equal_T1(self):
        self.assertEqual(add_document_and_put_on_shelf('11-11', 'Ivanova Daria', 'passport', '3'),
                         f'Документ 11-11 добавлен на полку 3')
    def test_add_document_Equal_T2(self):
        self.assertEqual(add_document_and_put_on_shelf('10006', 'Ivanova Daria', 'passport', '3'),
                         f'Документ с номером: 10006 уже существует')
    def test_add_document_Equal_T3(self):
        self.assertEqual(add_document_and_put_on_shelf('333', 'Sazin Arseniy', 'passport', '5'),
                         f'Полки с таким номером не существует')
    def test_add_document_NotEqual_T1(self):
        self.assertNotEqual(add_document_and_put_on_shelf('11-11', 'Ivanova Daria', 'passport', '5'),
                            f'Документ 11-11 добавлен на полку 5')
    def test_add_document_NotEqual_T2(self):
        self.assertNotEqual(add_document_and_put_on_shelf('1000', 'Ivanova Daria', 'passport', '3'),
                            f'Документ с номером: 1000 уже существует')
    def test_add_document_NotEqual_T3(self):
        self.assertNotEqual(add_document_and_put_on_shelf('333', 'Sazin Arseniy', 'passport', '3'),
                            f'Полки с таким номером не существует')

    #delete_document_and_put_off_shelf
    def test_delete_document_Equal_T1(self):
        self.assertEqual(delete_document_and_put_off_shelf('11-2'),
                         f'Документ с номером: 11-2 удален')
    def test_delete_document_Equal_T2(self):
        self.assertEqual(delete_document_and_put_off_shelf('333'),
                         f'Документа с таким номером не существует')
    def test_delete_document_NotEqual_T1(self):
        self.assertNotEqual(delete_document_and_put_off_shelf('11-11'),
                            f'Документ с номером: 11-11 удален')
    def test_delete_document_NotEqual_T2(self):
        self.assertNotEqual(delete_document_and_put_off_shelf('2207 876234'),
                            f'Документа с таким номером не существует')

    #add_shelf
    def test_add_shelf_Equal_T1(self):
        self.assertEqual(add_shelf('5'),
                         f'Полка с номером 5 создана')
    def test_add_shelf_Equal_T2(self):
        self.assertEqual(add_shelf('1'),
                         f'Полка с таким номером уже существует')
    def test_add_shelf_NotEqual_T1(self):
        self.assertNotEqual(add_shelf('2'),
                            f'Полка с номером 2 создана')
    def test_add_shelf_NotEqual_T2(self):
        self.assertNotEqual(add_shelf('22'),
                            f'Полка с таким номером уже существует')


if __name__ == '__main__':
    unittest.main()
