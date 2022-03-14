import unittest
from json_manipulator import process_file, process_text
from errors import ManipulationException

class TestUtils(unittest.TestCase):

    def test_when_single_key_update(self):
        result = process_file("test-json.json", "myKey", "test")

        self.assertEqual(result["myKey"], "test")

    def test_when_nested_key_update(self):
        result = process_file("test-json.json", "myNestedObject.myNestedKey", "test")

        self.assertEqual(result["myNestedObject"]["myNestedKey"], "test")

    def test_when_key_is_array_update_all(self):
        result = process_file("test-json.json", "myArray.myNestedArrayKey", "test")

        self.assertEqual(result["myArray"][0]["myNestedArrayKey"], "test")
        self.assertEqual(result["myArray"][1]["myNestedArrayKey"], "test")

    def test_when_invalid_key_throw_exception(self):
        with self.assertRaises(ManipulationException) as cm:
            process_file("test-json.json", "nonexistent", "test")

        self.assertEqual(cm.exception.code, "INVALID_KEY_PATH")

    def test_when_last_key_is_not_primitive_throw_exception(self):
        with self.assertRaises(ManipulationException) as cm:
            process_file("test-json.json", "myNestedObject", "test")

        self.assertEqual(cm.exception.code, "INVALID_LAST_KEY_TYPE")

    def test_when_not_last_key_is_primitive_throw_exception(self):
        with self.assertRaises(ManipulationException) as cm:
            process_file("test-json.json", "myNestedObject.myNestedKey.nonexistent", "test")

        self.assertEqual(cm.exception.code, "INVALID_MIDDLE_KEY_TYPE")

    def test_when_file_invalid_throw_exception(self):
        with self.assertRaises(ManipulationException) as cm:
            process_file("nonexistent.json", "insightMetadata.activated", "test")

        self.assertEqual(cm.exception.code, "INPUT_INVALID_FILE")

    def test_when_json_invalid_throw_exception(self):
        with self.assertRaises(ManipulationException) as cm:
            process_text("{", "insightMetadata.activated", "test")

        self.assertEqual(cm.exception.code, "INPUT_INVALID_JSON")