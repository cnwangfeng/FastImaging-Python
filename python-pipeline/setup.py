#!/usr/bin/env python

from setuptools import setup, find_packages
import versioneer

install_requires = [
        'astropy',
        'click',
        'pandas',
]

setup(
        name="fastimgproto",
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        packages=find_packages(),
        include_package_data=True,
        # description="Utility scripts ",
        author="Tim Staley",
        author_email="github@timstaley.co.uk",
        # url="https://github.com/",
        install_requires=install_requires,
        entry_points='''
            [console_scripts]
            fastimg_extract_lsm=fastimgproto.scripts.extract_lsm:cli
            fastimg_fullpipe=fastimgproto.scripts.fullpipe:cli
        ''',
)
