from setuptools import setup, find_packages

setup(
    name='pyoscal',
    version='0.9.0',
    include_package_data=True,
    description='Python Library for Reading and writing OSCAL Files',
    url='https://gitlab.com/shrgroup/oss/python/pyoscal',
    author='SHR Emerging Technologies',
    author_email='emerging.technologies@shrgroupllc.com',
    license='Apache 2.0',
    packages=find_packages(),
    install_requires=[
        'lxml'
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9'
    ],
)
