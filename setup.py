"""Setup script for the emailhunterclient package."""

from setuptools import find_packages, setup

setup(
    name='emailhunterclient',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'emailhunter=emailhunter.main:main',
        ],
    },
)
