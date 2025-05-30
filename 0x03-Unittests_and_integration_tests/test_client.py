#!/usr/bin/env python3
"""Unittests for the GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test suite for GithubOrgClient methods."""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, org_name):
        """
        Test the `org` property of GithubOrgClient.

        Ensures that get_json is called with the correct URL
        and that the result matches the expected organization data.
        """
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

    def test_public_repos_url(self):
        """
        Test the `_public_repos_url` property.

        Ensures that it returns the mocked URL using PropertyMock.
        """
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_property:
            mock_property.return_value = "mocked_url"
            client = GithubOrgClient("test_org")

            self.assertEqual(client._public_repos_url, "mocked_url")
            mock_property.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test the `public_repos` method.

        Mocks the get_json method and _public_repos_url property
        to ensure correct parsing of repository names.
        """
        mock_get_json.return_value = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None}
        ]

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/abc"
            client = GithubOrgClient("test_org")

            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with(
                "https://api.github.com/orgs/abc"
            )
            mock_url.assert_called_once()

    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        client = GithubOrgClient("test_org")

        result = client.has_license(repo, license_key)
        self.assertEqual(result, expected)