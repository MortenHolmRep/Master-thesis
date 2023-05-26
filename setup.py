"""Setup script for DFTBBoost."""

from setuptools import setup, find_packages

SETUP_REQUIRES = [
    "setuptools>=60.0",
]

# https://pypi.org/classifiers/
CLASSIFIERS = {
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3.8",
    "Environment :: CPU",
    "Enviornment :: GPU",
}

INSTALL_REQUIRES = [
    "matplotlib",
    "numpy",
    "pandas",
    "sciki-learn",
    "scipy",
    "pysmiles",
    "plotly",
    "tqdm",
    "torchmetrics",
    "networkx",

torchmetrics >= 0.11.0

EXTRAS_REQUIRE = {
    "develop": [
        "black",
        "flake8",
        "docformatter",
        "isort",
        "mypy",
        "autopep8",
        "pre-commit"
    ]
    "GPU": [
        "torch @ https://download.pytorch.org/whl/cu118'",
        "torch_geometric >= 2.2",
        "optuna",
    ],
    "CPU": [
        "torch",
        "torch_geometric >= 2.2",
        "optuna",
    ],
}

setup(
    name='DFTBBoost',
    version='0.1.0',
    author='Søren Langkidle',
    author_email='soeren@langkilde.com',
    packages=find_packages(),
    setup_requires=SETUP_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    dependency_links=["./source"],
    extras_require=EXTRAS_REQUIRE,
    classifier=CLASSIFIERS,
)
