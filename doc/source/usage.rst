Usage
=====

This package provides a `Solver` class that can be used to solve a linear system of equations.

Solve a linear system
--------------------

Import the package and `numpy`:

.. code-block:: python

    import example_package_samreynoldsmath as mypkg
    import numpy as np

Create a new `Solver` object and set up the linear system:

.. code-block:: python

    solver = mypkg.Solver(A=np.array([[1, 2], [3, 4]]), b=np.array([1, 2]))

The `solve()` method returns the solution to the linear system:

.. code-block:: python

    x = solver.solve()
