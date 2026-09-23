from setuptools import setup, find_packages

setup(
    name="fibdemo",
    version="0.0.1",
    description="FastAPI Fibonacci API and matplotlib plot client",
    package_dir={"": "src"},
    py_modules=["server", "client"],
    python_requires=">=3.12",
    install_requires=[
        "fastapi>=0.110",
        "uvicorn[standard]>=0.29",
        "requests>=2.31",
        "matplotlib>=3.8",
    ],
)

