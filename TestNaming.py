﻿from main import name_generator, calc_height, get_date
import unittest


class TestName(unittest.TestCase):
    def test_placeholder(self):
        name = calc_height(1, 2)
        self.assertEqual(name, "H1-H2")

    def test_should_end_with_gsa(self):
        name = name_generator(1, 2)
        self.assertTrue(name.endswith(".gsa"))

    def test_should_include_date(self):
        name = name_generator(1, 2, True)
        date = name.split("_")[0]
        self.assertTrue(date.isdigit())
        self.assertTrue(len(date) == 8)
        self.assertTrue("_" in name)

    def test_should_not_include_date(self):
        name = name_generator(1, 2, False)
        self.assertFalse("_" in name)

    def test_date_should_have_underscore(self):
        date = get_date()
        self.assertTrue(date.endswith("_"))

    def test_should_have_second_height_first(self):
        name = calc_height(1, 2, False)
        self.assertEqual(name, "H2-H1")

    def test_should_only_have_first_structure_when_second_is_zero(self):
        name = calc_height(1, 0)
        self.assertEqual(name, "H1")


if __name__ == '__main__':
    unittest.main()
