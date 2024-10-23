from operator import attrgetter
from os import path
from setuptools import setup

def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()

def from_here(relative_path):
    return path.join(path.dirname(__file__), relative_path)

def get_requirements(filename='requirements.txt'):
    """Read requirements from requirements.txt"""
    requirements = []
    if path.exists(filename):
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if line.startswith('-e '):
                        requirements.append(line.split('#egg=')[1])
                    else:
                        requirements.append(line)
    return requirements

setup(
    name="win10toast",
    version="0.9",
    install_requires=get_requirements(from_here("requirements.txt")),
    packages=["win10toast"],
    license="BSD",
    url="https://github.com/jithurjacob/Windows-10-Toast-Notifications",
    download_url='https://github.com/jithurjacob/Windows-10-Toast-Notifications/tarball/0.9',
    description=(
        "An easy-to-use Python library for displaying "
        "Windows 10 Toast Notifications"
    ),
    include_package_data=True,
    package_data={
        '': ['*.txt'],
        'win10toast': ['data/*.ico'],
    },
    long_description=read('README.md'),
    long_description_content_type="text/markdown",  # Added to properly render README on PyPI
    author="Jithu R Jacob",
    author_email="jithurjacob@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        'Operating System :: Microsoft',
        'Environment :: Win32 (MS Windows)',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",  # Added to specify Python version requirement
)
