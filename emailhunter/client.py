"""Client module for Email Hunter.

This module provides a client interface to interact with various Email Hunter API endpoints,
allowing for email verification, domain search, and email finding.
"""

import requests


class EmailHunterClient(object):
    """Client for interacting with the Email Hunter API.

    This client provides methods to communicate with the Email Hunter API for
    performing tasks such as email verification, domain search, and email finding.
    """

    def __init__(self, api_key: str):
        """Initialize the client with the given API key.

        Args:
            api_key (str): The API key for authenticating with the Email Hunter API.
        """
        self.api_key = api_key
        self.base_url = 'https://api.hunter.io/v2/'

    def domain_search(self, domain: str) -> dict:
        """Search for email addresses associated with a given domain.

        Args:
            domain (str): The domain for which to search email addresses.

        Returns:
            dict: The search results from the API.
        """
        url = ''.join([self.base_url, 'domain-search'])
        api_request_params = {'domain': domain, 'api_key': self.api_key}
        response = requests.get(url, params=api_request_params, timeout=5)
        return response.json()

    def email_finder(self, first_name: str, last_name: str, domain: str) -> dict:
        """Find the most likely email address for a person given their name and a domain.

        Args:
            domain (str): The domain associated with the person's email address.
            first_name (str): The first name of the person.
            last_name (str): The last name of the person.

        Returns:
            dict: The found email address and related information.
        """
        url = ''.join([self.base_url, 'email-finder'])
        api_request_params = {
            'first_name': first_name,
            'last_name': last_name,
            'domain': domain,
            'api_key': self.api_key,
        }
        response = requests.get(url, params=api_request_params, timeout=5)
        return response.json()

    def email_verifier(self, email: str) -> dict:
        """Verify the deliverability of an email address using the Email Hunter API.

        Args:
            email (str): The email address to be verified.

        Returns:
            dict: The verification result from the API.
        """
        url = ''.join([self.base_url, 'email-verifier'])
        api_request_params = {'email': email, 'api_key': self.api_key}
        response = requests.get(url, params=api_request_params, timeout=5)
        return response.json()
