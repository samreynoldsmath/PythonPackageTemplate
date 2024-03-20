"""
example_package_samreynoldsmath
===============================

This is a simple example package that contains a single class, `Solver`, which
solves a linear system of equations. The package also contains a test suite
that can be run with `pytest`.
"""

from .solver import Solver

__all__ = ["Solver"]
