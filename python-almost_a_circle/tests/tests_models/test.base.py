import unittest
from models.base import Base, Rectangle, Square


class TestBase(unittest.TestCase):

    def test_to_json_string(self):
        """Test when input is an empty list"""
        self.assertEqual(Base.to_json_string([]), "[]")

        """Test when input is a list of dictionaries"""
        input_list = [{"id": 1, "name": "Matt"}, {"id": 2, "name": "Bob"}]
        expect_output = '[{"id": 1, "name": "Matt"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(Base.to_json_string(input_list), expect_output)

    def test_save_to_file_not_none(self):
        """Test when list_objs is None"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])

        with open('Rectangle.json', 'r') as f:
            expected_json = (
               '[{"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}, '
               '{"id": 2, "width": 3, "height": 4, "x": 0, "y": 0}]')
            self.assertEqual(f.read(), expected_json)

    def test_from_json_string(self):
        """Test when JSON string is empty"""
        self.assertEqual(Base.from_json_string(""), [])

        """Test when JSON string is not empty"""
        json_string = '[{"id": 1, "name": "Matt"}, {"id": 2, "name": "Bob"}]'
        expected_output = [{"id": 1, "name": "Matt"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(Base.from_json_string(json_string), expected_output)

    def test_create(self):
        """Test creating a Rectangle instance"""
        r_dict = {"id": 1, "width": 2, "height": 3}
        r = Rectangle.create(**r_dict)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 0/0 - 2/3")

        """Test creating a Square instance"""
        s_dict = {"id": 2, "size": 4}
        s = Square.create(**s_dict)
        self.assertEqual(s.__str__(), "[Square] (2) 0/0 - 4")

    def test_load_from_file(self):
        """ Test loading from a non-existent file"""
        self.assertEqual(Rectangle.load_from_file(), [])

        """Test loading from an existing file"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(3, 4)
        Rectangle.save_to_file([r1, r2])
        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertEqual(loaded_rectangles[0].__str__(),
                         "[Rectangle] (1) 0/0 - 1/2")
        self.assertEqual(loaded_rectangles[1].__str__(),
                         "[Rectangle] (2) 0/0 - 3/4")
