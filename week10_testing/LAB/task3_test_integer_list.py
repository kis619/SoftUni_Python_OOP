from classes.integer import IntegerList

from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.integer = IntegerList(0, 1, 2)

    def test_init_integers(self):
        self.assertEqual([0, 1, 2], self.integer._IntegerList__data)

    def test_init_non_integers(self):
        integer = IntegerList(False, 1.2, "kr")
        self.assertEqual([], integer._IntegerList__data)

    def test_add_with_integer(self):
        self.assertEqual([0, 1, 2, 6], self.integer.add(6))

    def test_add_with_non_integer(self):
        with self.assertRaises(ValueError) as error:
            self.integer.add(2.1)
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_remove_index_valid(self):
        self.assertEqual(2, self.integer.remove_index(2))

    def test_remove_index_invalid(self):
        with self.assertRaises(IndexError) as error:
            self.integer.remove_index(10)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_valid_index(self):
        self.assertEqual(0, self.integer.get(0))

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError) as error:
            self.integer.get(10)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_valid_index(self):
        self.integer.insert(0, 25)
        self.assertEqual([25, 0, 1, 2], self.integer._IntegerList__data)

    def test_insert_index_invalid(self):
        with self.assertRaises(ValueError) as error:
            self.integer.insert(1, "hey")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_index_out_of_range(self):
        with self.assertRaises(IndexError) as error:
            self.integer.insert(5, 1)
        self.assertEqual("Index is out of range", str(error.exception))

    def test_get_biggest(self):
        self.assertEqual(2, self.integer.get_biggest())

    def test_get_index(self):
        self.assertEqual(0, self.integer.get_index(0))


if __name__ == "__main__":
    main()
