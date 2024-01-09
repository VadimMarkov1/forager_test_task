"""Main module for Email Hunter client demonstration."""

from emailhunter.client import EmailHunterClient
from emailhunter.storage import EmailStorageService


def main():
    """Run the main application."""
    email_hunter_client = EmailHunterClient('test-api-key')
    storage_service = EmailStorageService()

    verifier_result = email_hunter_client.email_verifier('contact@example.com')
    storage_service.add(verifier_result)

    log(storage_service.get_all())

    domain_result = email_hunter_client.domain_search('example.com')
    storage_service.add(domain_result)

    finder_result = email_hunter_client.email_finder('John', 'Doe', 'example.com')
    storage_service.add(finder_result)

    log(storage_service.get_all())

    storage_service.delete_all()
    log(storage_service.storage)


def log(message):
    """Log a message to the console."""
    print(message)


if __name__ == '__main__':
    main()
