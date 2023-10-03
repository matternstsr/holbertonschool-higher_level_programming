import unittest
from base import Base


class TestBase(unittest.TestCase):
    def test_init_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_init_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_to_json_string(self):
        obj = Base()
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string([obj.to_dictionary()]),
                         '[{"id": 1}]')

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        obj_list = [obj1, obj2]
        Base.save_to_file(obj_list)

        with open("Base.json", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

    def test_from_json_string(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        obj_list = Base.from_json_string(json_str)
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 2)

    def test_create(self):
        dictionary = {'id': 3}
        obj = Base.create(**dictionary)
        self.assertEqual(obj.id, 3)

    def test_load_from_file(self):
        with open("Base.json", "w", encoding="utf-8") as f:
            f.write('[{"id": 4}, {"id": 5}]')
        obj_list = Base.load_from_file()
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 4)
        self.assertEqual(obj_list[1].id, 5)
