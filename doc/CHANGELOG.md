# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- [x] `doc/` directory containing documentation files
- [x] `doc/source/` directory containing Sphinx configuration files
- [x] `.readthedocs.yml` file for configuring ReadTheDocs
- [x] new dev dependency `myst-parser` for parsing markdown files in Sphinx

### Changed
- [x] `README.md` to include a link to the documentation
- [x] move `CHANGELOG.md` to the `doc/` directory


## [0.2.1] - 2024-04-01

### Added

- `.github/workflows` directory with a `pylint.yml` file for running `pylint` on the codebase

### Changed

- [x] move Jacobi solver to a new module to test refactoring

## v0.1.4 - v0.1.16
- [x] struggle to understand why `pip` would not install the package dependencies when installing from `test.pypi.org`, but finally realize that it does when installing from `pypi.org`
- [x] update the installation instructions in `README.md` to reflect the correct installation process
- [x] update the `pyproject.toml` file to include the correct package metadata
- [x] switch to using `poetry` for building and publishing the package

## v0.1.3
- [x] add `numpy` to `build-system.requires` in `pyproject.toml`

## v0.1.2
- [x] try cleaning the `dist` directory before building the package

## v0.1.1
- [x] add `numpy` to dependencies in `pyproject.toml`
- [x] update installation instructions in `README.md`

## v0.1.0
## Features
- [x] add a module
- [x] add a test
- [x] configure `pylint`