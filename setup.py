from setuptools import setup, find_packages
setup(
    name='MyCommand',
    version='0.1.0',
    entry_points={'console_scripts': ['MyCommand = App.command1:main']},
    install_requires=[
        'click'
    ],
    packages=find_packages()
    )