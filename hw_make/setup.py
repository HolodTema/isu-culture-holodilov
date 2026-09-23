from setuptools import setup, find_packages

setup(
    name="fibonacci-server-plots",
    version="0.0.1",
    description="FastAPI Fibonacci API and matplotlib plot client",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12",
