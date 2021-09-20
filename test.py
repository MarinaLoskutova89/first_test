import unittest
from app import get_name_by_document_number, check_document_existance

class TestSomething(unittest.TestCase):
    def check_document_existance(self):
        self.assertTrue(check_document_existance('11-2'), True)
    # def test_strings_a_3(self):
    #     self.assertEqual(multiplication_string('a', 3), 'aaa')
if __name__ == '__main__':
    unittest.main()
