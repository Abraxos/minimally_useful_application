# Development Guide

To develop the minimally useful application, you will need several tools described here. Assuming you have cloned the directory, you will want to set up a virtual environment to run the code in, then install the module "in place", and finally as you make your changes you will write, run, and generate coverage review of your tests. All of the tools that allow you to do this are listed below, the main incantation to remember is this one:

```
(minimally_useful_application) $ nosetests --cover-package=minimally_useful_application --with-coverage
```

## Development Setup

Assuming that you have cloned the git repository, you will need to create a virtual environment first. The Python virtualenv is greatly augmented by a system of scripts called the virtualenvwrapper. There are detailed instructions on how to install it below, but in general you will want to do something like this:

```
$ mkvirtualenv --python=/usr/bin/python3 minimally_useful_application
(minimally_useful_application) $
```

Once your virtual environment is set up, it will be activated as the default virtualenv in that particular shell. In this document, all commands executed from inside a virtualenv will be preceded by something like this: `(minimally_useful_application) $` because that is what it will look like in the terminal. After this, you will be able to execute the following incantation to load the virtualenv from anywhere:

```
$ workon minimally_useful_application
(minimally_useful_application) $
```

Once inside the virtualenv you can install the package you're working on using `pip` and the `-e` parameter which allows the installation to be "in-place". This adds the current module directory to the path thereby making development easier since you can change the code and execute any entry points instantly. This will also install any required packages based on your `setup.py` file.

```
(minimally_useful_application)$ pip install -e <path to package>
```

To run an entry point, you can now simply call it:

```
(minimally_useful_application) $ mua-timing
```

You then need to install `nose` and `cover` inside the virtualenv to be able to run unit tests:

```
(minimally_useful_application) $ pip install nose cover
```

From the top-level repo directory, you can execute nosetests like so (which will also generage coverage reports and place them in the `cover/` directory):

```
(minimally_useful_application) $ nosetests --cover-package=minimally_useful_application --with-coverage
```

## Useful Development Tools

### Virtualenvwrapper

Installation instructions: https://virtualenvwrapper.readthedocs.io/en/latest/install.html

### Pylint

PyLint is a particularly important and useful tool for developing large Python projects. I strongly advise using it on all projects written in python. It provides static analysis of a Python program to determine if there are any common bugs or style violations. It can be installed like so:

```
(minimally_useful_application) $ pip install pylint
```

It can then be run on your code like so:

```
(minimally_useful_application) $ pylint minimally_useful_application
```

The end result is a report that details any errors and gives you a score based on various stylistic requirements in Python. I strongly advise integrating Pylint into your IDE and using it constantly. I personally prefer my code to have a flawless pylint rating as this eliminates the potential for a LOT of common Python bugs that plague large projects.

### NoseTests

```
(minimally_useful_application) $ pip install nose
```

#### Coverage

```
(minimally_useful_application) $ pip install coverage
```
