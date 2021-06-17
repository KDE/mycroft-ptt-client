""" Install the mycroft_ptt_client package
"""
from setuptools import setup

setup(
    name='mycroft_ptt_client',
    version='0.0.1',
    url='https://github.com/AIIX/mycroft_ptt_client',
    keywords='mycroft ptt daemon client',
    packages=['mycroft_ptt_client'],
    install_requires=['python-libinput', 'mycroft-messagebus-client'],
    include_package_data=True,
    license='Apache',
    author='Aditya Mehra',
    author_email='aix.m@outlook.com',
    description='Mycroft Push-To-Talk Client',
    entry_points={
        'console_scripts': [
            'mycroft_ptt_client=mycroft_ptt_client.__main__:main',
            ]
        }
)
