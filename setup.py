from setuptools import setup, find_packages
from pathlib import Path

setup(
    name="stringth",
    version="0.0.1",
    license="Apache-2.0",
    author="taennan",
    author_email="taennan@scoobyapps.com",
    description="Converts to and from nth strings and integers",
    long_description=Path("./README.md").read_text(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=["string", "str", "nth"],
    classifiers=[
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ]
)
