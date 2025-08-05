from setuptools import setup, find_packages

setup(
    name='my-python-app',
    version='0.1.0',
    author='p4r53c',
    author_email='your.email@example.com',
    description='GHA BP TEST',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/p4r53c/oidc-jf-test',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'certifi==2024.8.30',
        'cffi==1.17.1',
        'cryptography==43.0.3',
        'pycparser==2.22'

    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
