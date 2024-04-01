"""
jacobi.py
=========

This module contains the jacobi_preconditioned_solve function for solving Ax=b
using Jacobi preconditioning.
"""

import numpy as np

def jacobi_preconditioned_solve(A: np.ndarray, b: np.ndarray):
    """
    Solve Ax=b using Jacobi preconditioning.
    """
    if not isinstance(A, np.ndarray) or not isinstance(b, np.ndarray):
        raise TypeError("A and b must be numpy arrays")
    if A.shape[0] != A.shape[1]:
        raise ValueError("A must be square")
    if A.shape[0] != b.shape[0]:
        raise ValueError("A and b must have the same number of rows")
    D = np.diag(A)
    D_inv = np.diag(1 / D)
    return np.linalg.solve(D_inv @ A, D_inv @ b)