# Python Package Template

## Description
A simple demo of how to structure, use, and publish a Python package.

## Prerequisites
- Python 3.11 or later
- [Virtual environments](https://virtualenv.pypa.io/en/latest/user_guide.html)
- A [PyPi](https://pypi.org/) account
- [poetry](https://python-poetry.org/)

## Usage
### Clone the repository
- This is a template repository on [GitHub](https://github.com/samreynoldsmath/PythonPackageTemplate)
- To use it, click the green `Use this template` button at the top of the GitHub page
- Clone your new repository to your local machine

### Make changes
- Change the package name from `example_package_samreynoldsmath` to your own package name by renaming the directory
- Edit the source code as needed
- Update the `pyproject.toml` file to include your own package metadata
- Update `README.md`, `CHANGELOG.md`, `LICENSE`, `.gitignore`, and other files as needed

### Build and upload
Clear the `dist` directory
```bash
rm dist/*
```
Build the package using `poetry`
```bash
poetry build
```
Publish the package to [PyPi](https://pypi.org/) using `poetry`
```bash
poetry publish
```

### Install
In a fresh virtual environment, install the package using `pip` (replace `example-package-samreynoldsmath` with your package name)
```bash
pip install example-package-samreynoldsmath
```

## Documentation
See documentation for this package on [readthedocs.io](https://pythonpackagetemplate.readthedocs.io/en/latest/index.html).

Want to make documentation for your project? Check out the [tutorial](https://docs.readthedocs.io/en/stable/tutorial/).

## License
[MIT](https://choosealicense.com/licenses/mit/)
