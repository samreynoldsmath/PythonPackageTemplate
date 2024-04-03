Usage
=====

.. _installation:

Installation
------------

You can install the package from PyPI using pip:

.. code-block:: console

   (.venv) $ pip install example_package_samreynoldsmath

Set up linear system
--------------------

Create a new `Solver` object and set up the linear system:

.. code-block:: python

    import example_package_samreynoldsmath as mypkg
    import numpy as np

    solver = mypkg.Solver(A=np.array([[1, 2], [3, 4]]), b=np.array([1, 2]))

    x = solver.solve()

The `solve` method returns the solution to the linear system.
