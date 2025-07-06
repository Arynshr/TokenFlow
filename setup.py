from setuptools import setup, find_packages

setup(
    name = "Tokenflow",
    version = "1",
    packages = find_packages(where = "src"),
    package_dir = {"":"src"},
    python_requires = ">=3.7",
)
