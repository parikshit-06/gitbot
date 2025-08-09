from setuptools import setup, find_packages

setup(
    name='gitbot',
    version='0.1.0',
    description='Context-aware git command helper CLI tool',
    author='Parikshit Sonwane',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gitbot=gitbot.cli:main',
        ],
    },
    install_requires=[],
    python_requires='>=3.7',
)
