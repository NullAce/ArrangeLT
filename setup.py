from setuptools import setup, find_packages

setup(
    name='arrangelt',
    version='0.2.0',
    author='Austin Pratt',
    author_email='183548723+NullAce@users.noreply.github.com',
    description='A Python library for sorting and organizing files.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NullAce/arrangelt',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license='Apache License 2.0',
    license_files=['LICENSE'],
)