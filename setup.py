from setuptools import find_packages, setup

setup(
    name='chatgpt',
    version='0.0.0',
    description='This package creates a cli for the openai api',
    author='Reid Williams',
    url='https://github.com/reidwil/opencli',
    install_requires=open('requirements.txt', 'r').read(),
    packages=find_packages(exclude=('tests*')),
    entry_points={
        'console_scripts': [
            'opencli = src.cli:cli'
        ]
    }
)