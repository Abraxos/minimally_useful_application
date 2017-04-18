# Minimally Useful Application

This project is meant as a template for how to begin, structure, develop, test, and deploy a python application using standard or commonly accepted tools. I will be updating this application as I learn more interesting tools.

## Project Structure

The approximate structure of your project should be something like this:

```
minimally_useful_application/
├── DEVELOP.md
├── LICENSE
├── Makefile
├── README.md
├── docs
│   └── Overview.md
├── minimally_useful_application
│   ├── __init__.py
│   ├── core.py
│   ├── timing
│   │   ├── __init__.py
│   │   └── timing.py
│   └── utils
│       ├── __init__.py
│       ├── cli_utils.py
│       ├── config_utils.py
│       └── file_utils.py
├── requirements.txt
├── setup.py
├── something.ini
└── tests
    ├── test_advanced.py
    └── test_basic.py
```

The files in the root directory of your project should be as follows:

+ **DEVELOP.md** - This file should include your development setup information. It can be in any format, although GitHub and most git-based tools are partial to Markdown: https://daringfireball.net/projects/markdown/syntax. Note that the DEVELOP.md file for this project is not empty, it describes the recommended approach to configuring a virtual environment for this project.
+ **LICENSE** - This should contain the text of the license that you chose to use for your project.
+ **README.md** - The basic readme for your project. This should describe the purpose of your project, provide relevant links, examples, and installation information for an average user. For this project the `README.md` file is kind of the exception since it describes all the core information about the project that makes it relevant. Nevertheless, it does contain installation information at the bottom.
+ **requirements.txt** - This file should contain the python packages required for your particular project.
+ **setup.py** - This file is used by Python's setup tools for most of the important information about your project. More on this below.

## Source Code ("main" directory)

This is where the code for your application should live. Note that the entry point for your program should be a function called `main()` which is called at the bottom of the file with the following code:

```python
if __name__ == '__main__':
    main()
```

You can see this put to use in the file `core.py`. Another thing to note is that any directory with a `__init__.py` file is considered a module. Therefore every source code directory should have such a file.

### Command Line Arguments

A key element of most programs is the ability to input command-line arguments into your application. Python is no exception. There is a module called `argparse` which provides a lot of functionality for this purpose. You should really check out the documentation here: https://docs.python.org/3/library/argparse.html but I included some basic examples in this application.

There are multiple examples of useful functionality in the `utils/cli_utils.py` file which are not necessarily useful in this application but are nevertheless very useful in general (like, for example, readable directory argument validation).

### Configuration

The configuration of your application can vary depending on your specific needs, but the standard way of handing configurations is as `.ini` files which can be parsed by Python's `configparser` module. The `utils/config_utils.py` file has some good examples for how to use it and there is an example configuration file called `config.ini`

### Subdirectories

Your project should include (at least) the following subdirectories:

+ **docs** - This is where any relevant documentation should live (with the exception of your `README.md` and `DEVELOP.md` files). Specifically, if you have extensive documentation for your source code that is likely auto-generated, it should be placed in this directory.
+ **tests** - This is where all of your tests should go. Pretty self explanatory (more on testing below)
+ **project** - The source code should live in a directory that has the same name as your actual project. While in most configurations this would produce a situation where your code would live in a directory called `my_project/my_project`, its nevertheless useful because it allows the developer to safely clone the repo to something with a different name. So, for example, if I chose to clone the repo into a folder called `stuff`, I would still have `stuff/my_project`. Inside of this directory you should organize your code as is appropriate for your particular project. In my case I chose to isolate common utilities into a folder called `utils/`.

## Setup

The setup of a particular python module is handled via the `setup.py` file, which in turn uses the `distutils` package. The setup file should have all the information necessary to actually install your module on a system using `pip`. It should look something like this:

```python
'''Setup file for the minimally_useful_application program.'''
from setuptools import setup, find_packages


with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

with open('requirements.txt') as f:
    REQUIREMENTS = f.readlines()

setup(
    name='minimally_useful_application',
    version='0.1.0',
    description='A minimally useful application demonstrating common \
                 requirements for a program in Python.',
    long_description=README,
    author='Eugene Kovalev',
    author_email='euge.kovalev@gmail.com',
    url='https://github.com/Abraxos/minimally_useful_application',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=REQUIREMENTS,
    entry_points={'console_scripts' : ['mua-timing = minimally_useful_application.core:main']}
)

```

While some of the key elements are described below, the critical thing that this file gives you is that once you've cloned this repository (assuming you've cloned it to a folder called `minimally_useful_application/` as is the default), you should be able to execute the following command to install it on your system:

```
$ pip install minimally_useful_application/
```

Now, there are many variations on what you can do here depending on what you're trying to accomplish. For example, if you're installing the application for a whole system, you will likely need root privileges:

```
$ sudo pip install minimally_useful_application/
```

or you could install it just for your specific user:

```
$ pip install --user minimally_useful_application/
```

Alternatively, you could install it "in place" which is highly useful for developers because it points python's path directly at the files in question allowing you to edit them and test them live without having to reinstall:

```
$ pip install -e minimally_useful_application/
```

### Requirements

*source: https://packaging.python.org/requirements/*

Requirements should be written to a file, one per line, called `requirements.txt`. These are the other Python modules that need to be installed on the system. If you install the module using `pip` as shown above, it should automatically find and download these requirements. This particular project has only one requirement, the `arrow` library that it uses for timing functionality.

### Entry Points

*source: https://chriswarrick.com/blog/2014/09/15/python-apps-the-right-way-entry_points-and-scripts/*

Entry points are a particularly useful feature of the setup file. Specifically, they allow you to automatically make functions of your module to become available as console commands.

The key element that allows this is:

```python
entry_points={'console_scripts' : ['mua-timing = minimally_useful_application.core:main']}
```

This means that if you install the `minimally_useful_application` as described above using `pip`, you will be able to execute the `main()` function of the `core.py` file by calling:

```
$ mua-timing
```

### Additional Files

https://docs.python.org/3.6/distutils/setupscript.html#installing-additional-files

TODO: Finish this section

## Tests

TODO: Write up testing standards and examples (don't forget coverage tools)

## Docs

TODO: Write up something about documentation generators.
