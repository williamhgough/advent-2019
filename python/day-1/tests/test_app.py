import unittest
from app import (
    calculate_fuel,
    calculate_fuel_for_fuel,
    process_inputs,
    part1,
    part2
)


class TestApp(unittest.TestCase):
    def test_calculate_fuel(self):
        self.assertEqual(calculate_fuel(12), 2)
        self.assertEqual(calculate_fuel(14), 2)
        self.assertEqual(calculate_fuel(1969), 654)
        self.assertEqual(calculate_fuel(100756), 33583)

    def test_calculate_fuel_for_fuel(self):
        self.assertEqual(calculate_fuel_for_fuel(1969), 966)
        self.assertEqual(calculate_fuel_for_fuel(100756), 50346)

    def test_process_inputs_normal(self):
        lst = ["100756", "1969", "14"]
        self.assertEqual(process_inputs(lst, calculate_fuel), [33583, 654, 2])

    def test_process_inputs_normal(self):
        lst = ["100756", "1969"]
        self.assertEqual(process_inputs(
            lst, calculate_fuel_for_fuel), [50346, 966])

    def test_part1(self):
        lst = ["100756", "1969", "14"]
        self.assertEqual(part1(lst), 34239)

    def test_part2(self):
        lst = ["100756", "1969"]
        self.assertEqual(part2(lst), 51312)


if __name__ == "__main__":
    unittest.main()
