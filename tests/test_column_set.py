import unittest
from unittest import TestCase

from column_set import ColumnSet


class TestColumnSet(TestCase):

    def test_create_with_valid_list(self):

        columns = ['a', 'b', 'c']
        column_set = ColumnSet(columns=columns)
        self.assertDictEqual(
            d1={'a': 'a', 'b': 'b', 'c': 'c'},
            d2=column_set._columns
        )

    def test_create_with_invalid_list(self):

        columns = ['a', 'b', 'a']
        self.assertRaises(ValueError, ColumnSet, columns)

    def test_create_with_dict(self):

        columns = {'a': 'A', 'b': 'B', 'c': 'C'}
        column_set = ColumnSet(columns=columns)
        self.assertDictEqual(columns, column_set._columns)

    def test_add_no_overlaps(self):

        columns_1 = {'a': 'A', 'b': 'B', 'c': 'C'}
        column_set_1 = ColumnSet(columns_1)
        columns_2 = {'d': 'D', 'e': 'E', 'f': 'F'}
        column_set_2 = ColumnSet(columns_2)
        combined = column_set_1 + column_set_2
        expected = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F'}
        self.assertDictEqual(
            d1=expected,
            d2=combined._columns
        )

    def test_with_overlaps(self):

        columns_1 = {'a': 'A', 'b': 'B', 'c': 'C'}
        column_set_1 = ColumnSet(columns_1)
        columns_2 = {'c': 'C', 'd': 'D', 'e': 'E'}
        column_set_2 = ColumnSet(columns_2)
        self.assertRaises(KeyError, column_set_1.__add__, column_set_2)


if __name__ == '__main__':

    unittest.main()
