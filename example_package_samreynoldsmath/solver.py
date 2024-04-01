"""
solver.py
=========

This module contains the Solver class for solving Ax=b, and was mostly written
Copilot. Good job, Copilot!
"""

import numpy as np

from .jacobi import jacobi_preconditioned_solve


class Solver:
    """
    Solver class for solving Ax=b.
    """

    n: int
    A: np.ndarray
    b: np.ndarray

    def __init__(self, A: np.ndarray, b: np.ndarray):
        """
        Initialize the Solver class with A and b.
        """
        self.check_shape(A, b)
        self.A = A
        self.b = b

    def check_shape(self, A: np.ndarray, b: np.ndarray):
        """
        Check that A and b have the correct shape.
        """
        self.n = A.shape[0]
        if A.shape[1] != self.n:
            raise ValueError("A must be square")
        if b.shape[0] != self.n:
            raise ValueError("A and b must have the same number of rows")

    def solve(self):
        """
        Solve Ax=b.
        """
        return np.linalg.solve(self.A, self.b)

    def jacobi_preconditioned_solve(self):
        """
        Solve Ax=b using Jacobi preconditioning.
        """
        return jacobi_preconditioned_solve(self.A, self.b)
