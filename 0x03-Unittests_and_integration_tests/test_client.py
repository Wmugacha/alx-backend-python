#!/usr/bin/env python3

import unittest
from client import GithubOrgClient
from utils import access_nested_map, get_json, memoize
from unittest.mock import Mock, patch
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name):

        mock_org_data = {
            "login": org_name,
            "name": f"{org_name.title()} Organization",
            "description": f"Test organization for {org_name}",
            "public_repos": 100,
            "repos_url": f"https://api.github.com/orgs/{org_name}/repos",
            "url": f"https://api.github.com/orgs/{org_name}",
            "followers": 50,
            "following": 25
        }

        with patch('client.get_json') as mock_get_json:
            mock_get_json.return_value = mock_org_data

            client = GithubOrgClient(org_name)

            result = client.org

            self.assertEqual(result, mock_org_data)
            self.assertIsInstance(result, dict)

            expected_url = f"https://api.github.com/orgs/{org_name}"
            mock_get_json.assert_called_once_with(expected_url)