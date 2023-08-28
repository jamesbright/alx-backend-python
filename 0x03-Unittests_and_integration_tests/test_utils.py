#!/usr/bin/env python3
""" Test SUITE Unittest module Task """

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """ Class that tests nested map functions """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """ Method returns test result """
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)