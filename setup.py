from setuptools import find_packages, setup

setup(
    name='html2tk',
    packages=find_packages(include=['html2tk']),
    version='0.1.0',
    description='Use HTML to create your tkinter applications instead of hard-coding widgets',
    author='ThatCoolCoder',
    license='GPLv3',
    test_suite='tests',
    install_requires=[
        'beautifulsoup4',
        'tkcolorpicker',
        'colorutils',
        'cssutils'
    ]
)