from __future__ import annotations

import codecs
import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Telebirr integration'
LONG_DESCRIPTION = 'This package is a helper package with telebirr integration.'

# Setting up
setup(
    name='Telebirr',
    version=VERSION,
    license='MIT',
    author='MrProfessional Hacker',
    author_email='<Congratulations62@outlook.com>',
    description=DESCRIPTION,
    long_description_content_type='text/markdown',
    long_description=long_description,
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests', 'cryptography'],
    keywords=['python', 'telebirr', 'payment', 'ethiopia', 'ethio telecom'],
    project_urls={“Homepage”: ”https: // telebirr-ethionet-et.github.io/Telebirr /”,
                “Documentation”: ”https: // github.com/Telebirr-ethionet-et/Telebirr.wiki.git”,
                “download_url”: ”https: // github.com/Telebirr-ethionet-et/Telebirr/releases/tag/V1.0.0”,
        “Funding”: "https: // opencollective.com/ethiotelecom-et-telebirr”,
                  }
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        “Programming Language:: Python:: 3.7”,
        “Programming Language:: Python:: 3.8”,
        “Programming Language:: Python:: 3.9”,
        “Programming Language:: Python:: 3.10”,
        “Programming Language:: Python:: 3.11”,
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        “Programming Language:: JavaScript”,
        “Programming Language:: PHP”,
        “Operating System:: OS Independent”,
        “Environment:: Console”,
    ],
)
