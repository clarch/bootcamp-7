"""Test suite for super_sum."""
from unittest import TestCase
from super_sum import super_sum

class SuperSumTestCase(TestCase):
	"""Test Case for super sum"""
	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_empty_input(self):
		"""Test empty input."""
		self.assertEqual(
			super_sum(), 0)

	def test_sum_of_integers(self):
		"""Test sum of integers."""
		self.assertEqual(super_sum(1, 2, 3), 6)
		self.assertNotEqual(super_sum(-1, 1), 2)

	def test_sum_of_one_item(self):
		"""Test sum of one item."""
		self.assertEqual(super_sum(1), 1)

	def test_for_a_string(self):
		"""Test for a string input."""
		self.assertEqual(super_sum(7, "May", 8), 0)

	def test_for_a_list(self):
		"""Test for a string input."""
		self.assertEqual(super_sum([9, 1, 2]), 12)

	