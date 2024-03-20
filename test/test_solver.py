import sys
import os

import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import mypackage

TOL = 1e-12

def test_solver():
    """Test the Solver class."""
    A = np.array([[1, 2], [3, 4]])
    b = np.array([5, 6])
    solver = mypackage.Solver(A, b)
    x = solver.solve()
    assert np.linalg.norm(A @ x - b) < TOL
    x = solver.jacobi_preconditioned_solve()
    assert np.linalg.norm(A @ x - b) < TOL
