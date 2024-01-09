"""Storage module for Email Hunter.

This module provides a simple in-memory storage solution for storing and managing
results of email verification and other operations performed using the Email Hunter API.
"""


class EmailStorageService(object):
    """Service for storing and managing email verification and other operations results."""

    def __init__(self):
        """Initialize the storage with an empty dictionary."""
        self.storage = []

    def add(self, result_data: dict):
        """Add a new result to the storage.

        Args:
            result_data (dict): The result of the email verification.
        """
        self.storage.append(result_data)

    def get_all(self):
        """Retrieve an email verification result from the storage."""
        return self.storage

    def delete_all(self):
        """Clear all data from the storage."""
        self.storage = []
