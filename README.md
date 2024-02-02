# mds_array_manipulation

[![Documentation Status](https://readthedocs.org/projects/mds-array-manipulation/badge/?version=latest)](https://mds-array-manipulation.readthedocs.io/en/latest/?badge=latest) [![ci-cd](https://github.com/UBC-MDS/mds_array_manipulation/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/UBC-MDS/mds_array_manipulation/actions/workflows/ci-cd.yml) ![release](https://img.shields.io/github/release-date/UBC-MDS/mds_array_manipulation) ![version](https://img.shields.io/github/v/release/UBC-MDS/mds_array_manipulation) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Python 3.9.0](https://img.shields.io/badge/python-3.9.0-blue.svg)](https://www.python.org/downloads/release/python-390/)

## Summary

### Project Summary

The package is intended to do array manipulations functions like Searching, Sorting, Counting non-zero elements, Finding indices of max value. 
This is a package developed for the group-17 project for the UBC MDS DSCI 524 (Collaborative Software Development) course.

### Functions Included in the Package

- `sort_array`: Takes a numpy array of integers or strings and returns the array in sorted order

- `search_array`: Searches for and returns the index of a specified element in a numpy array, if it exists

- `count_nonzero_elements`: Count the number of non zero elements in an array

- `argmax`: Returns the index of the max element in the array

### Fit into the Python Ecosystem

There are several Python packages focused on array manipulation, such as numpy, which are used for a wide range of array manipulation. However, the package aims to recreate some of the basic array operations available in the [numpy package](https://github.com/numpy/numpy).
  
## Installation

Note: This package is currently under development and not yet available on PyPI. To install, please clone the repository and install the package locally. Follow the below instructions to install the package.

1. Clone the github repository using:
```bash
https://github.com/UBC-MDS/mds_array_manipulation.git
```
2. Run the below commands to create the virual environment:
```bash
$ conda create --name mds_array_manipulation python=3.9 -y
$ conda activate mds_array_manipulation
```
3. You can install `mds_array_manipulation` package using `poetry`
```
$ poetry install
```
If you dont have poetry installed in your base environment, you can follow the [installation guide](https://python-poetry.org/docs/#installation) for poetry.

4. To get the coverage report, run the following code:
```
poetry run pytest tests/ --cov=src/mds_array_manipulation/
```

### Future Update

Once the package is full developed and published to PyPI, you can use it using below command:

```bash
$ pip install mds_array_manipulation
```

## Features

Contains functions: Searching, Sorting, Counting non-zero elements, Finding indices of max value. This package is a group-17 project for the UBC MDS DSCI 524 (Collaborative Software Development) course.

## Dependencies

- Python 3 or greater

## Usage

Example usage:
```bash
>>> import numpy as np
>>> from mds_array_manipulation.search_array import search_array
>>> from mds_array_manipulation.argmax import argmax
>>> from mds_array_manipulation.sort_array import sort_array
>>> from mds_array_manipulation.count_nonzero_elements import count_nonzero_elements

>>> arr = np.array([20, 10, 40, 30, 50, 90, 60])
>>> search_array(arr, 50)
    4
>>> argmax(arr)
    5
>>> sort_array(arr)
    array([10, 20, 30, 40, 50, 60, 90])
>>> count_nonzero_elements(arr)
    {'Total Non-Zero Elements in Array': 7}
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Contributors

* Sean McKay - @sean-m-mckay
* Kittipong Wongwipasamitkun (Jo) - @jokittipong
* Yan Zeng - @Owl64901
* Aishwarya Nadimpally - @Aishwarya120111

## License

`mds_array_manipulation` was created by Kittipong Wongwipasamitkun, Sean Mckay, Yan Zeng, Aishwarya Nadimpally. It is licensed under the terms of the MIT license.

## Credits

`mds_array_manipulation` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
