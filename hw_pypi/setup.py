from setuptools import setup, find_packages

setup(
    name="fibapp",
    version="0.0.1",
    description="FastAPI Fibonacci API and matplotlib plot client",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HolodTema/isu-culture-holodilov/tree/feature/hw/pypi",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.12",
    install_requires=[
        "fastapi>=0.110",
        "uvicorn[standard]>=0.29",
        "requests>=2.31",
        "matplotlib>=3.8",
    ],
    entry_points={
        "console_scripts": [
            "fib-server=fibapp.server:run",
            "fib-client=fibapp.client:main",
            "fib-demo=fibapp.demo:main",
        ],
    },
)

