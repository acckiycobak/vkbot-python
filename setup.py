import io
from os import path

from setuptools import setup, find_packages

import bot

here = path.abspath(path.dirname(__file__))


def long_description():
    with io.open(file=path.join(here, "README.md"), encoding="utf-8") as file:
        return file.read()


def requirements():
    with io.open(file=path.join(here, "requirements.txt")) as file:
        return file.readlines()


setup(
    name="mailru-im-bot",
    version=bot.__version__,
    description="Pure Python interface for Bot API. Bot cookbook for Humans.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/mail-ru-im/bot-python",
    author="ICQ LLC (Mail.Ru Group)",
    author_email="support@icq.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    keywords="mailru im bot api",
    packages=find_packages(exclude=["example"]),
    install_requires=requirements(),
    python_requires=">= 3.6",
    include_package_data=True,
    zip_safe=False
)
