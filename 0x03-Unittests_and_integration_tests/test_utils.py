#!/usr/bin/env python3
"""
Unit tests for functions in the utils module.

This module contains test classes for `access_nested_map`, `get_json`,
and `memoize` functions, ensuring their correctness and expected behavior.
"""

import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Test suite for the `access_nested_map` function.

    This class provides tests to ensure that `access_nested_map` correctly
    retrieves values from deeply nested dictionaries and handles invalid paths.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests that `access_nested_map` returns the correct value
        for a given nested map and valid path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Tests that `access_nested_map` raises a KeyError
        when an invalid path is provided or a key does not exist.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
    Test suite for the `get_json` function.

    This class ensures that `get_json` correctly fetches and parses
    JSON data from a URL by mocking external HTTP requests.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Tests that `get_json` returns the expected JSON payload
        for given URLs by mocking `requests.get`.
        """
        # Use patch as a context manager to mock 'requests.get'
        with patch('utils.requests.get') as mock_get:
            # Create a mock response object and configure its json() method
            # to return the desired test_payload.
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            # Configure the mocked 'requests.get' to return our mock_response.
            mock_get.return_value = mock_response

            # Call the function under test.
            result = get_json(test_url)

            # Assert that the function returned the expected payload.
            self.assertEqual(result, test_payload)
            # Verify that 'requests.get' was called exactly once.
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
    Test suite for the `memoize` decorator.

    This class verifies that the `memoize` decorator correctly caches
    the results of a method call, preventing redundant computations.
    """

    def test_memoize(self):
        """
        Tests that the `memoize` decorator caches the result of a method call,
        while ensuring the decorated method is only called once.
        """
        class TestClass:
            """
            A nested class used to test the `memoize` decorator's behavior
            on (`a_property`) that relies on (`a_method`).
            """
            def a_method(self):
                """
                A simple method that will be mocked to track its calls.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A method decorated with `memoize` that calls `a_method`.
                Its result should be cached after the first call.
                """
                return self.a_method()

        # Create an instance of the TestClass.
        test_obj = TestClass()

        # Patch 'a_method' on the specific instance of TestClass.
        with patch.object(test_obj, 'a_method') as mock_a_method:
            # Configure the mocked 'a_method' to return a specific value.
            mock_a_method.return_value = "mocked_result"

            # First call to the memoized property/method.
            # This should trigger a call to 'a_method'.
            first_result = test_obj.a_property
            self.assertEqual(first_result, "mocked_result")
            # Assert that 'a_method' was called exactly once.
            mock_a_method.assert_called_once()

            # Reset the mock's call history.
            # This is crucial to verify that 'a_method' is NOT called again.
            mock_a_method.reset_mock()

            # Second call to the memoized property/method.
            # This should get the result from the cache and NOT call a_method.
            second_result = test_obj.a_property
            self.assertEqual(second_result, "mocked_result")
            # Assert that 'a_method' was NOT called this time.
            mock_a_method.assert_not_called()
