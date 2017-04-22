import os
from setuptools import setup, find_packages
import halma
from halma.examples import available
#Grab the README.md for the long description
with open('README.rst', 'r') as f:
    long_description = f.read()


VERSION = halma.__version__

def setup_package():
    examples = set()
    for i in available():
        if not os.path.isdir('halma/examples/' + i):
            if '.' in i:
                glob_name = 'examples/*.' + i.split('.')[-1]
            else:
                glob_name = 'examples/' + i
        else:
            glob_name = 'examples/' + i + '/*'
        examples.add(glob_name)

    setup(
        name = "halma",
        version = VERSION,
        author = "Kelvin Rodriguez",
        author_email = "kr788@nau.edu",
        description = ("A Halama AI agent for NAU's AI class"),
        long_description = long_description,
        license = "Public Domain",
        keywords = "NAU",
        url = "http://packages.python.org/halma",
        packages=find_packages(),
        include_package_data=True,
        package_data={'autocnet' : list(examples)},
        zip_safe=False,
        install_requires=[],
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Topic :: Utilities",
            "License :: Public Domain",
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
    )

if __name__ == '__main__':
    setup_package()
