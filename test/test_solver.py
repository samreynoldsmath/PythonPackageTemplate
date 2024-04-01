"""
test_solver.py
==============

Tests for the Solver class.
"""

import numpy as np

import example_package_samreynoldsmath as pkg # pylint: disable=import-error

TOL = 1e-12

def test_solver():
    """Test the Solver class."""
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    solver = pkg.Solver(A, b)
    x = solver.solve()
    assert np.linalg.norm(A @ x - b) < TOL
    x = solver.jacobi_preconditioned_solve()
    assert np.linalg.norm(A @ x - b) < TOL
