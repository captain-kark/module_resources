import pathlib
from setuptools import setup

# This call to setup() does all the work
setup(
    name="module-resources",
    version="0.0.1",
    description="Import non-python files in a project directory as python namedtuple objects.",
    long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/captain-kark/module_resources",
    author="Andrew Yurisich",
    author_email="andrew.yurisich@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["module_resources"],
    extras_require={
        'yaml': ['pyyaml']
    }
)
