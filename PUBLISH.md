# PUBLISH
Taken from the tutorial at https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Dependencies
```bash
python3 -m pip install --upgrade twine build
```

## Build
```bash
python3 -m build
```

## Upload to PyPi
### test.pypi.org
```bash
python3 -m twine upload --repository testpypi dist/*
```

### pypi.org
```bash
python3 -m twine upload dist/*
```

## Install
### test.pypi.org
```bash
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-package-samreynoldsmath
```
### pypi.org
```bash
pip install example-package-samreynoldsmath
```
