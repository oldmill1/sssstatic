# ./setup.py
from setuptools import setup, find_packages

setup(
    name="sssstatic",
    version="0.1.0",
    description="A Simple Static Site Generator",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sssstatic=sssstatic:main",
        ],
    },
    python_requires=">=3.6",
    install_requires=[
        "rich>=10.0.0",
    ],
)
