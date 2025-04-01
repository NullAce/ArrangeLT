from setuptools import setup, find_packages

setup(
    name='pysort',
    version='0.1.2',
    author='Austin Pratt',
    author_email='183548723+NullAce@users.noreply.github.com',
    description='A python file sorting library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/NullAce/PySort',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',  # Updated license classifier
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    license_files=['LICENSE'],  # Ensure your LICENSE file is included
)