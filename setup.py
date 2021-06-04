from setuptools import setup
from Cython.Build import cythonize


# ""
name = "find_servers"
setup(ext_modules=cythonize(f"{name}.pyx", #f"{name}_cy.py",
                            annotate=True))